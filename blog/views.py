from django.shortcuts import render
from django.http import JsonResponse
from blog.models import Post
import json
from django.http import HttpResponse
import datetime
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")
def index(request):

	data = Post.objects.all()
	posts_as_dict = []
	for post in data:
	    post_as_dict = {
	        'title' : post.title,
	        'body' : post.body,
	        'date' : post.date}
	    posts_as_dict.append(post_as_dict)
	json_data = json.dumps(posts_as_dict, default=json_serial)
	collection.insert_one(posts_as_dict[0]).inserted_id
	print json_data
	return HttpResponse(json_data, content_type='application/json')
	# return json.dumps(data, default=json_serial)