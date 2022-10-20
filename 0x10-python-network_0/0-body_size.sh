#!/usr/bin/env bash
#prints the size of a server response in bytes
curl -s $1 | wc -c
