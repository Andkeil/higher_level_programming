#!/bin/bash
#Script Take URL, send POST req, display body of response
curl $1 -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
