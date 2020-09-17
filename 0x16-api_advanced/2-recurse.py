#!/usr/bin/python3
"""
recursive
"""
import requests
i = -1
a = []
flag = 0
n = ""


def lenghtgetter(f, hot_list=[]):
    """fde function"""
    leng = len(f)
    global i
    if leng - 1 == i:
        return hot_list
    else:
        i = i + 1
        hot_list.append(f[i]["data"]['title'])
        lenghtgetter(f, hot_list)
    return hot_list


def recurse(subreddit, hot_list=[]):
    """function return the number of subscribers of subreddit"""
    global a
    global flag
    global n
    global i
    useragent = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
    urll = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    if flag == 0:
        url = urll
    if flag == 1:
        url = urll + "?after=" + str(n)
    r = requests.get(url, headers={'User-agent': useragent})
    try:
        n = r.json()["data"]['after']
        try:
            f = r.json()["data"]['children']
            i = -1
            a = a + lenghtgetter(f, hot_list=[])
            if n is None:
                flag = 0
            else:
                flag = 1
                recurse(subreddit, hot_list=[])
        except KeyError:
            return (None)
    except BaseException:
        return (None)
    return a
