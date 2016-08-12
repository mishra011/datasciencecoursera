print  "hello"

from elasticsearch import Elasticsearch
es = Elasticsearch()

res = es.indices.create(index='test-index', ignore=400)

print (res['created'])


