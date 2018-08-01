#!/bin/bash
#Script Take URL and display all HTTP methods available
curl -sI "$1" | grep "Allow"| cut -d ' ' -f 2-
