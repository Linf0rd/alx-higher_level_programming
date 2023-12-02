#!/bin/bash
# This Bash script takes in a URL, sends a GET request to the URL, displaying the body of the response for 200 OK
curl -sL "$1" -w "%{http_code}" | grep "200" && curl -sL "$1"
