#!/bin/bash
# Thiz servea as a comment for all
curl -sI "$1" | grep "Allow" | cut -d" " -f2-
