#!/bin/bash
# This script displays all HTTP methods the server will accept.
curl -sIX OPTIONS "$1" | grep -w 'Allow' | cut -d ' ' -f2-
