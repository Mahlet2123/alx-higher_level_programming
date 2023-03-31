#!/bin/bash
# prints status code
curl -sI -o /dev/NULL -w "%{http_code}" $1
