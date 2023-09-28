#!/bin/bash

# Check if URL has been provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

# Send a request to the URL and display the size of the body of the response
curl -s "$1" | wc -c
