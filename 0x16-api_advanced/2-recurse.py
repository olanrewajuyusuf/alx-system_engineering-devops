#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """returns a list containing the titles of all hot articles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    header = {'User-Agent': 'olanre 0x16-api_advanced'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    response = requests.get(url, headers=headers, params=params allow_redirects=False)
    if response.status_code == 404:
        return 0
    res = response.json().get('data')
    after = res.get('after')
    count += res.get('dist')
    for i in res.get('children'):
        hot_list.append(i.get('data').get('title'))

    if after is not none:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
