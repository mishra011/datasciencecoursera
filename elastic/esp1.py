import csv
from elasticsearch import Elasticsearch
es = Elasticsearch()

res = es.indices.create(index = "sad")
print res['created']
with open("sample1.csv") as f:
	reader = csv.DictReader(f)
	for line in reader:
		es.index(index="sad",doc_type = "user", body =line)


"""
to get by index

es.index(index="sad", doc_type="user", id=22)

for further query

s = Search(using = client, index = "sad")\
	.filter("term" , category = "search" )\
	.query("match",title = "python")\
	.query(~Q("match", biblography = "anaconda"))

s.aggs.bucket('per_tag', 'terms', field = 'tags')\
	.metric('super_stars','avg',field ='stars')

"""