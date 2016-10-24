import certifi
import sys
import os
import json
import time
import config as Config
from flask import Flask
from pprint import pprint
from elasticsearch import Elasticsearch
from flask import Flask, request, render_template, g, redirect, Response, make_response, jsonify

application = Flask(__name__)  
app = application

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search/<keyword>', methods=['GET'])
def search(keyword):

    try:
        es = Elasticsearch([Config.ES])
        TWITTER_APP_KEY = Config.TWITTER_APP_KEY
        TWITTER_APP_KEY_SECRET = Config.TWITTER_APP_KEY_SECRET
        TWITTER_ACCESS_TOKEN = Config.TWITTER_ACCESS_TOKEN
        TWITTER_ACCESS_TOKEN_SECRET = Config.TWITTER_ACCESS_TOKEN_SECRET

        res = es.search(index="twitter-index",size=10000, sort='timestamp:desc', body={"query": {"match": { "text": { "query": keyword, "operator": "or" } } } })
        output=[]
        for doc in res["hits"]["hits"]:
            output.append(doc['_source']['location'])
        return Response(json.dumps(output), content_type='application/json')
    except e :
        pass

if __name__ == "__main__":         

	try:
		 app.run(threaded=True)
	except Exception as e:
		pass
	else:
		 pass
	finally:
		 pass
