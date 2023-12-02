#!/bin/bash
# Get the byte size of an HTTP response header for a URL.
curl -s "$1" | wc -c
