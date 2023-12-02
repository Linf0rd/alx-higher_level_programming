#!/bin/bash
# This Bash script takes in a URL, sends a GET request to the URL, displaying the body of the response for 200 OK
curl -sLf "$1" -X GET
