log_id=$1

permalink='http://172.16.28.25:9000/messages/graylog_0/'$log_id''

#uthe user who creates the card in their board
api_key=$(sh quote_remove.sh `cat url_params.json | jq '.key'`)

api_token==$(sh quote_remove.sh `cat url_params.json | jq '.token'`)

list_id==$(sh quote_remove.sh `cat url_params.json | jq '.idList'`)

card_name==$(sh quote_remove.sh `cat url_params.json | jq '.name'`)


count=`curl --request GET --url 'https://api.trello.com/1/lists/'$list_id'/cards?key='$api_key'&token='$api_token'' | grep -c "$card_name"`
if [ $count -eq 0 ]
then

	card_id_temp=`curl --request POST --url 'https://api.trello.com/1/cards/' -H 'Content-Type: application/json' --data @url_params.json | jq '.id'`
	
	if [ $? -ne 0 ]
	then
		echo "card isn't created"
	else

		echo "card created"
		
		card_id=`sh quote_remove.sh $card_id_temp`

		curl --request POST --url 'https://api.trello.com/1/cards/'$card_id'/attachments?key='$api_key'&token='$api_token'&url='$permalink'&name=Permalink'
	
		if [ $? -ne 0 ]
		then
        	echo "Permalink not created"
		else
			echo "Permalink created"
		fi
	
	fi
fi
