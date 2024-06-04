#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'olanre 0x16-api_advanced'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        return 0
    res = response.json().get('data')
    [print(x.get('data').get('title')) for x in res.get('children')]
