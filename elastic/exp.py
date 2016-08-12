from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(send_get_body_as='POST')

doc = {
    'author': 'Maruti India',
    'text': 'maruti launches a new car',
    'timestamp': datetime.now(),
}
res = es.index(index="maruti", doc_type='cars', id=1, body=doc)
print(res['created'])

res = es.get(index="maruti", doc_type='cars', id=1)
print(res['_source'])

es.indices.refresh(index="maruti")

res = es.search(index="maruti", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

