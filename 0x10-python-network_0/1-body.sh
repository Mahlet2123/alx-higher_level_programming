#!/bin/bash
# Display only body of a 200 status code response
curl -s -L -w "\n%{http_code}\n" $1
