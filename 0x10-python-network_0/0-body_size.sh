#!/bin/bash
# Sxript that curl a site and display content length
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
