#!/bin/bash
# This script displays all HTTP methods the server will accept.
curl -sX POST -d @$2 -H "Content-Type: application/json" $1
