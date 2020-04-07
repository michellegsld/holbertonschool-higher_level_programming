#!/bin/bash
# Sends a POST request and two variables
curl -s-X POST $1 -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
