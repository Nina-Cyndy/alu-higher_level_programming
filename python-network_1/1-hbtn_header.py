#!/usr/bin/python3
"""
Script that takes in a URL, sends a request and displays the X-Request-Id value
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            print(response.headers.get('X-Request-Id'))
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} - {e.reason}")
