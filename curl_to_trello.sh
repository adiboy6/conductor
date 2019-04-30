card_name=$1
card_desc=$2
list_id=$3
api_key=''
api_token=''
count=`curl --request GET   --url 'https://api.trello.com/1/lists/'$list_id'/cards?key='$api_key'&token='$api_token'' | grep -c "$card_name"`
if [ $count -eq 0 ]
then
curl --request POST \
  --url 'https://api.trello.com/1/cards?name='$card_name'&desc='$card_desc'&pos=top&idList='$list_id'&keepFromSource=all&key='$api_key'&token='$api_token''
  fi
