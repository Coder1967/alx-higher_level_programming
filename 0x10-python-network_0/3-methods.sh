#!/bin/bash
#prints all the methods allowed by server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
