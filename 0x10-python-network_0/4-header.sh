#!/bin/bash
#sends a get method to the server with variabl 'X-School-User-Id' with value 98
curl -sH "X-HolbertonSchool-User-Id: 98" $1
