#!/bin/bash
#Script Take URL, send GET req, display body
curl -H "X-HolbertonSchool-User-Id: 98" -sX GET $1
