#!/bin/bash

echo "Test Starting..."

URL=""

for i in {1..101}
do
    echo "Sending request $i/101"
    curl -s -X POST $URL \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "name=Alex&hobbies=climbing,reading" \
    -w "\nStatus: %{http_code}\n"
done

echo "See that the app is recovering" 

sleep 1m

echo "Sending final request"
curl -s -X POST $URL \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "name=Boby&hobbies=climbing,reading, running" \
    -w "\nStatus: %{http_code}\n"

echo "Test Finished..."