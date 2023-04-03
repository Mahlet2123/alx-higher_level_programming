#!/bin/bash
# causes server to respond with a certain msg
curl -s -L -X PUT -H "Origin:HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
