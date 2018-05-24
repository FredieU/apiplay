#! /bin/bash

curl 'https://jsonplaceholder.typicode.com/users/7' | jq

./api.py

curl 'https://jsonplaceholder.typicode.com/users/7' | jq