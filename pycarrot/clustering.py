import atexit
import json
import os
import re
import subprocess
import sys
from typing import List

import psutil
import requests

from .document import Document


class Clustering:
    def __init__(self, port=8080):
        self.host = 'localhost'
        self.port = port
        self.path = os.path.dirname(os.path.abspath(__file__))
        if sys.platform == "win32":
            self.process = subprocess.Popen('cd %s& dcs.cmd -port=%d' %
                                            (os.path.join(self.path, 'dcs'), self.port), stdout=subprocess.PIPE,
                                            bufsize=1,
                                            shell=True, close_fds=True)
        else:
            self.process = subprocess.Popen('cd %s; sh dcs.sh -port=%d' %
                                            (os.path.join(self.path, 'dcs'), self.port), stdout=subprocess.PIPE,
                                            bufsize=1,
                                            shell=True, close_fds=True)
        for line in self.process.stdout:
            l = line.decode().strip()
            print(l)
            if 'DCS started on port' in l:
                self.port = int(re.findall(r'port: (.*?) \[', l)[0])
                atexit.register(self.kill_dcs)
                break

    def kill_dcs(self):
        for child in psutil.Process(self.process.pid).children(recursive=True):
            child.kill()
        self.process.terminate()
        self.process.kill()

    def cluster(self, documents: List[Document], algorithm: str = 'lingo'):
        """
        :param documents: List[Document]
        :param algorithm: String. Default set as lingo, Optional: lingo | kmeans | stc | url | source
        :return: Return Clusters list or raise an Exception.
        """
        if not isinstance(documents, list):
            raise ValueError("First parameter(documents) must be a list object.")
        if not all(map(lambda x: isinstance(x, Document), documents)):
            raise ValueError("All items in documents list must be a Document instance.")
        data = ''.join([doc() for doc in documents])
        data = '<searchresult><query>query</query>' + data + '</searchresult>'
        req = requests.post(url='http://%s:%d/dcs/rest' % (self.host, self.port),
                            data={'dcs.c2stream': data,
                                  'dcs.algorithm': algorithm,
                                  'dcs.output.format': 'JSON'})
        if req.status_code == 200:
            return json.loads(req.text)['clusters']
        else:
            error = req.text.split('pre>')[-2][:-2]
            raise Exception(error)
