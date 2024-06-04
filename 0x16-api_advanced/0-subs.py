#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """returns the num of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'olanre 0x16-api_advanced'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    res = response.json().get('data')
    return res.get('subscribers')
