from flask import Flask
from flask import request
import os
import json
import urllib

app = Flask(__name__)

hire=[{'onboarding','auth-server'},'5cc7d40ccb79a267e1e5644f']
engage=[{'data-processor','ats'},'5cc7d42140535067a619d36b']
nurture=[{'starfox','survey'},'5cc7d417e375a43d1a8bed84']

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
		
		idList=''
		if i['fields']['app_name'] in hire[0]:
			idList=hire[1]
		elif i['fields']['app_name'] in engage[0]:
			idList=engage[1]
		else:
			idList=nurture[1]

		os.system("sh curl_to_trello.sh "+card_name+" "+message+" "+idList)
		print("\n\n")
	return "Request Processed.\n"

@app.route('/')
def hello_world():
	return 'TICKETRAISE'

app.run(host='0.0.0.0',port=5000)
