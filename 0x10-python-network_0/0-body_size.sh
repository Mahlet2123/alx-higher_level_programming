#!/bin/bash

# Check if a URL was provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

# Send a request using curl and store the response body in a variable
response=$(curl -s -w '\n%{size_download}' $1)

# Extract the size of the response body from the last line of the response
size=$(echo "$response" | tail -n 1)

# Display the size of the response body in bytes
echo "$size"
