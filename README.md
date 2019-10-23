# pycarrot2
A python wrapper of carrot2 clustering server.

Compatible with Linux, macOS and Windows.

### Usage

Test example:

```bash
python3 example.py
```

Usage:

```python
from pycarrot import Clustering, Document

documents = [{'title':'1','url':'1','content':1},{'title':'2','url':'2','content':2}]

c = Clustering(port=8081)
docs = [Document(title=doc['title'], url=doc['url'], content=doc['content']) for doc in documents]

result = c.cluster(docs, algorithm='lingo')
# algorithm could be lingo\kmeans\stc\url\source
print(result)
```

### FAQ

**How to solve "Form too large"?**

The form you sent is too large and exceeds the default value.

Solution: Modify dcs/dcs.sh, add `-Dorg.eclipse.jetty.server.Request.maxFormContentSize=500000` between `java` and `$DCS_OPTS `.