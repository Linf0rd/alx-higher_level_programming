#!/bin/bash
# Displays the body of the response with a custom header.
curl -sH "X-School-User-Id: 98" "$1"
