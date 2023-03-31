#!/bin/bash
# Bash script that sends a DELETE request to the URL 
curl -sIX OPTIONS $1 | grep "Allow" | cut -d " " -f2-
