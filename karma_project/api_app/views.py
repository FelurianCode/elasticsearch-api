from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
import json
from bson import json_util
import bsonjs

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db= client.twitter


#testing mongo connection
def get_tweets(request):
	result_doc = db.tweets.find().limit(2)
	result_list = []
	for x in result_doc:
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
		result_dic['interpretaciones'] = x['interpretaciones']

		result_list.append(result_dic)


	#json_docs = json.loads(docs)
	return JsonResponse({'data': result_list}, status=200)
