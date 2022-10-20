#!/bin/bash
# calls a post request passing valued email=test@gmail.com
# and value subject=I will always be here for PLD
curl -sL -X POST -d 'email=test@gmail.com&subject=I will always be here for PLD'
