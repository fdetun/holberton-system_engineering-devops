#!/usr/bin/python3
"""
0-main
"""
import requests


def number_of_subscribers(subreddit):
    """function return the number of subscribers of subreddit"""
    useragent = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers={'User-agent': useragent})
    return (r.json()["data"]['subscribers'])
