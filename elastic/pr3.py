from elasticsearch import Elasticsearch
import json
es = Elasticsearch()

doc =[{
	'Book': 'Harry Potter',
	'Author': 'J K Rowling',
	'year': 2011,
	'volumes': 8


},{
	
	'Book': 'Game of thrones',
	'Author': 'RR Martin',
	'year': 2010,
	'volumes': 10

}, {
	
	'Book': 'The tale of two cities',
	'Author': 'Chals Dickens',
	'year': 2003,
	'volumes': 3

}]
"""
for i in range(1,len(doc)+1):
	res = es.index(index="practise",doc_type="writing",id = i, body = doc[i-1])

print(res['created'])
"""
#res = es.mget(index="practise",doc_type="writing", body = {"ids":[1,2,3]} , _source = True, realtime = True)
res = es.get_source(index= "practise", doc_type="writing", id="3"	)

#res = es.search(index= "practise", doc_type="writing")
res = es.suggest(index= "practise", body = doc)
#print (res['_source'])

es.indices.refresh(index="practise")

#res = es.search(index = "practise",body = {"query":{"match_all":{}}})

res = json.dumps(res, indent = 4, sort_keys = True)
es.indices.refresh(index="practise")

print res 
"""
print("we got %d Hits:" %res['hits']['total'])

for hit in res['hits']['hits']:
	print ("%(Book)s %(Author)s %(year)d %(volumes)d " %hit["_source"])
"""

"""
import json
r = requests.get('http://localhost:9200') 
i = 1
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    es.index(index='practise', doc_type='writing', id=i, body=doc)
    i=i+1
 
print(i)

"""