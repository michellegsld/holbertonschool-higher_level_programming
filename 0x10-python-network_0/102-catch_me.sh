#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me and tries to find a certain message
curl -sL -X PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"
