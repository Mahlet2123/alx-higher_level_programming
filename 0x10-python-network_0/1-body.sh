#!/bin/bash
# sends a req to a URL and displays size of response
curl -s -L -w "\n%{http_code}\n" $1 | sed -n '/^200$/{:a;n;p;ba;}'
