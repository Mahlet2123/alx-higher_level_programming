#!/bin/bash
# This script displays all HTTP methods the server will accept.
curl -sX POST -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' "$1"
