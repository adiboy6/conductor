card_name=$1
card_desc=$2
list_id=5cb9694910047783d9aa7a10
count=`curl --request GET   --url 'https://api.trello.com/1/lists/'$list_id'/cards?key=f6dff15a20b77f79814e8331f507adc5&token=b7659470f6f04e8d31d8b3cb3807994d30aed92ed64696fd99bfbf8a4ded4a8a' | grep -c "$card_name"`
if [ $count -eq 0 ]
then
curl --request POST \
  --url 'https://api.trello.com/1/cards?name='$card_name'&desc='$card_desc'&pos=top&idList='$list_id'&keepFromSource=all&key=f6dff15a20b77f79814e8331f507adc5&token=b7659470f6f04e8d31d8b3cb3807994d30aed92ed64696fd99bfbf8a4ded4a8a'
  fi
