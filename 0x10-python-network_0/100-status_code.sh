#!/bin/bash
# status code only
curl $1 -o /dev/null -w '%{http_code}' -s
