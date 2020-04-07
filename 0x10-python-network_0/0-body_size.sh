#!/bin/bash
# Displays the size of the body of the response

curl -sI 0.0.0.0:5000 | grep Content-Length | cut -d " " -f 2
