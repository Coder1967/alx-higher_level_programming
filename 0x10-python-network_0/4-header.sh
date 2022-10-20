#!/bin/bash
#sends a get method to the server with a variable
curl -sX GET -H "X-School-User-Id: 98" $1
