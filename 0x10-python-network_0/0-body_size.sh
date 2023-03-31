#!/bin/bash
# sends a req to a URL and displays size of response
curl -s -w '%{size_download}\n' $1
