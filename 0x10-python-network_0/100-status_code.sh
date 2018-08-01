#!/bin/bash
#Script Take URL display status code of response
curl $1 -sI -w '%{http_code}' -o /dev/null
