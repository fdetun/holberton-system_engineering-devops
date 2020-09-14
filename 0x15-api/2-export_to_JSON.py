#!/usr/bin/python3
"""gathering from json and exprong ot to csv"""
import json
import requests
import sys


def getfunc(url):
    """ function to rturn json format from url"""
    r = requests.get(url)
    f = r.json()
    return f


if __name__ == "__main__":
    num = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(num)
    url2 = "https://jsonplaceholder.typicode.com/users?id={}".format(num)
    uname = getfunc(url2)[0]["username"]
    arr = []
    mydict = {"task": "", "completed": False, "username": uname}
    for i in getfunc(url):
        mydict = {}
        mydict["task"] = i["title"]
        mydict["completed"] = i["completed"]
        mydict["username"] = uname
        arr.append(mydict)
    my = {num: arr}
    with open(str(num) + ".json", 'w') as f:
        json.dump(my, f)
