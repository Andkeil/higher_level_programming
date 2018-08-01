#!/bin/bash
#Script take URL and display body
curl -Is $1 | grep Content-Length | cut -d ':' -f2 | sed 's/ //'
