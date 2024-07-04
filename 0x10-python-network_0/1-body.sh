#!/bin/bash
# Sends a GET request to the URL, and displays the response body
[ "$(curl -s -o /tmp/response_body -w "%{http_code}" "$1")" -eq 200 ] && cat /tmp/response_body; rm /tmp/response_body
