from elasticsearch import Elasticsearch

es = Elasticsearch()

doc ={
	'Book': 'Harry Potter',
	'Author': 'J K Rowling',
	'year': 2011,
	'volumes': 8


}

res = es.index(index="practise",doc_type="writing",id = 1, body = doc)

print(res['created'])

res = es.get(index="practise",doc_type="writing",id = 1)

print (res['_source'])

es.indices.refresh(index="practise")

res = es.search(index = "practise",body = {"query":{"match_all":{}}})

print("we got %d Hits:" %res['hits']['total'])

for hit in res['hits']['hits']:
	print ("%(Book)s %(Author)s %(year)d %(volumes)d " %hit["_source"])


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