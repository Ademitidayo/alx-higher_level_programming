#!/bin/bash
# Script that sends a request to a URL and displays only the response status code
curl -so /dev/null -w "%{http_code}" "$1"
