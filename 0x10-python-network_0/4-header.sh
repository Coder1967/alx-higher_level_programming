#!/bin/bash
#sends a get method to the server with variabl 'X-School-User-Id' with value 98
curl -sL -d 'X-School-User-Id=98' $1
