#!/bin/bash
# Bash script that takes in a URL, sends a request to the URL
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
