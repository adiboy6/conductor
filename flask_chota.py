from flask import Flask
from flask import request
import os
import json
import urllib

app = Flask(__name__)

@app.route("/trello", methods=["POST"])
def sendtoTrello():
	data1=request.json
	for i in data1['check_result']['matching_messages']:
		card_name=""
		message=urllib.quote(i["message"])
		if('caller_method_name' in i['fields']):
			if(i['fields']['caller_method_name']!='<init>'):
				card_name=(i['fields']['app_name']+"-"+i['fields']['caller_method_name'])
			else:
				card_name=(i['fields']['app_name']+"-"+i['fields']['caller_file_name'])
		else:
			card_name=(i['fields']['app_name']+"-"+i['fields']['logger_name'][i['fields']['logger_name'].rfind(".")+1:])
		os.system("sh curl_to_trello.sh "+card_name+" "+message)
		print("\n\n")
	return "Request Processed.\n"

@app.route('/')
def hello_world():
	return 'TICKETRAISE'

app.run(host='0.0.0.0',port=5000)
