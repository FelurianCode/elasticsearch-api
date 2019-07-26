from django.conf import settings
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from pymongo import MongoClient
from elasticsearch_dsl import *
from bson.json_util import dumps
import uuid 
from django.http import JsonResponse

# Create a connection to ElasticSearch
connections.create_connection()
client = MongoClient('localhost', 27017)
db= client.twitter
es = Elasticsearch()

def bulk_json_data(json_data, _index, doc_type):
    for doc in json_data:
    # use a `yield` generator so that the data
    # isn't loaded into memory
        if '{"index"' not in doc:
            yield {
                "_index": _index,
                "_type": doc_type,
                "_fielddata": True,
                "_id": uuid.uuid4(),
                "_source": doc
            }


def bulk_indexing(request):
	json_tweets = db.tweets.find()
	result_list = []
	for x in json_tweets:
		result_dic = {}
		result_dic['tweetId'] = x['tweetId']
		result_dic['queryId'] = x['queryId']
		result_dic['verb'] = x['verb']
		result_dic['busquedaId'] = x['busquedaId']
		result_dic['body'] = x['body']
		result_dic['link'] = x['link']
		result_dic['postedTime'] = x['postedTime'].strftime('%m/%d/%Y')
		result_dic['usuario'] = x['usuario']
		result_dic['aplicacion'] = x['aplicacion']
		result_dic['locacion'] = x['locacion']
		result_dic['hashtags'] = x['hashtags']
		result_dic['imagenes'] = x['imagenes']
		result_dic['urls'] = x['urls']
		result_dic['menciones'] = x['menciones']
		if 'interpretaciones' in x:
			result_dic['interpretaciones'] = x['interpretaciones']

		result_list.append(result_dic)
	

	try:
		response = bulk(client=es, actions=bulk_json_data(result_list, "tweets", "tweet"))
		print ("\nRESPONSE:", response)
		return JsonResponse({'response': dumps(response), 'result':  'Carga Exitosa'}, status=200)
	except Exception as e:
		return JsonResponse({'error': e}, status=400)

def search_by_date(request):
	s = Search(using=es).sort('-postedTime.keyword')
	response = s.execute()

	return JsonResponse({'response': response.to_dict()}, status=200)

def search_by_user(request):
	user = request.GET['user']
	s = Search(using=es).query("match", usuario__preferredUsername=user)
	response = s.execute()
	return JsonResponse({'response': response.to_dict()}, status=200)  
