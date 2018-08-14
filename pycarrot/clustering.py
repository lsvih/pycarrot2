import atexit
import json
import os
import re
import signal
import subprocess
from typing import List

import requests

from .document import Document


class Clustering:
    def __init__(self):
        self.host = 'localhost'
        self.port = 8080
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.process = subprocess.Popen('cd %s; sh dcs.sh' % os.path.join(self.path, 'dcs'), stdout=subprocess.PIPE,
                                        bufsize=1, shell=True, close_fds=True, preexec_fn=os.setsid)
        for line in self.process.stdout:
            l = line.decode().strip()
            print(l)
            if 'DCS started on port' in l:
                self.port = int(re.findall(r'port: (.*?) \[', l)[0])
                atexit.register(os.killpg, self.process.pid, signal.SIGUSR1)
                break

    def cluster(self, documents: List[Document], algorithm: str = 'lingo'):
        """
        :param documents: List[Document]
        :param algorithm: String. Default set as lingo, Optional: lingo | kmeans | stc | url | source
        :return: Return Clusters list or raise an Exception.
        """
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
