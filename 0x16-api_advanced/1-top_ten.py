#!/usr/bin/python3
"""
0-main
"""
import requests


def top_ten(subreddit):
    """function return the number of subscribers of subreddit"""
    useragent = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
    url = "https://www.reddit.com/r/{}/top/.json?limit=10".format(subreddit)
    r = requests.get(url, headers={'User-agent': useragent})
    try:
        f = r.json()["data"]['children']
        for i in f:
            print(i["data"]['title'])
    except BaseException:
        print(None)
