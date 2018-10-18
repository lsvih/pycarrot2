import json

from pycarrot import Clustering, Document

documents = json.loads(open('example.json', encoding='utf-8').read())['documents']

c = Clustering(port=8081)

docs = [Document(title=doc['title'], url=doc['url'], content=doc['content']) for doc in documents]

result = c.cluster(docs, algorithm='lingo')

print(result)
