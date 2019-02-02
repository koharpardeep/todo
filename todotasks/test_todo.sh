#!/bin/bash

#create To-do
echo "=========================Running for create todo ...================================================"
json=$(curl -X POST http://localhost:8000/todo/create/ -H 'cache-control: no-cache' -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' -F state=1 -F due_date=2018-01-05 -F 'text=Hi this is Pardeep Kumar6' | jq -r '.')

code=$( jq -r '.code' <<< "${json}")

if [ "$code" == "400" ]; then
	echo "Failed"
else
	echo "Success"
fi

echo "=========================create todo completed================================================"

echo "=========================Running for Get all todo ...================================================"
json=$(curl -s -X GET http://localhost:8000/todo/getall/?orderby=both | jq -r '.')


code=$( jq -r '.code' <<< "${json}")
data=$( jq -r '.data' <<< "${json}")
length=$( jq length <<< "${data}")

contentID=0

if [ "$length" -gt 0 ]; then
	contentID=$( jq -r '.[0].id' <<< "${data}")	
fi

if [ "$code" == "400" ]; then
	echo "Failed"
else
	echo $data | python -m json.tool
fi
echo "========================= Get all todo completed================================================"


echo "=========================Running for Update todo ...================================================"
if [ "$contentID" -gt 0 ]; then
json=$(curl -X POST http://localhost:8000/todo/update/ -H 'cache-control: no-cache' -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' -F id=$contentID -F state=1 -F due_date=2018-01-05 -F 'text=Hi this is Pardeep Kumar5' | jq -r '.')

code=$( jq -r '.code' <<< "${json}")

if [ "$code" == "400" ]; then
	echo "Failed"
else
	echo "Successfully Updated TODO with id $contentID"
fi
else
	echo "Zero TODO found"
fi

echo "=========================Update todo completed================================================"

echo "=========================Delete for Delete todo ...================================================"
if [ "$contentID" -gt 0 ]; then
json=$(curl -X POST http://localhost:8000/todo/delete/ -H 'cache-control: no-cache' -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' -F id=$contentID | jq -r '.')

code=$( jq -r '.code' <<< "${json}")

if [ "$code" == "400" ]; then
	echo "Failed"
else
	echo "Successfully Deleted TODO with id $contentID"
fi
else
	echo "Zero TODO found"
fi

echo "=========================Delete todo completed================================================"

echo "All tests completed"












