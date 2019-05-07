from flask import Flask
from flask import request
import os
import json
import urllib
import sys

app = Flask(__name__)

hire=[{'onboarding','auth-server'},'5cc7d40ccb79a267e1e5644f']
engage=[{'data-processor','ats'},'5cc7d42140535067a619d36b']
nurture=[{'starfox','survey'},'5cc7d417e375a43d1a8bed84']

@app.route("/trello", methods=["POST"])
def sendtoTrello():
	data1=request.json
	for i in data1['check_result']['matching_messages']:
		card_name=""
		description=urllib.quote(json.dumps(i))
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
		elif i['fields']['app_name'] in nurture[0]:
			idList=nurture[1]
		
		if idList!='':
			print ("creating a card:\n")	
			
			json_content={'key':'','token':'','idList':idList,'name':card_name,'desc':description]}
			
			with open('url_params.json','w') as json_content_temp:
				json.dump(json_content,json_content_temp)

			os.system("sh curl_to_trello.sh "+i["id"])
			print("\n\n")
		else:
			pass

	return "Request Processed.\n"

@app.route('/')
def hello_world():
	return 'TICKETRAISER'

app.run(host='0.0.0.0',port=5000)
