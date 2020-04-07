#!/bin/bash
# Sends a GET request and follows redirection to the end
curl -sL -X GET "$1"
