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
    url = "https://jsonplaceholder.typicode.com/todos?userId="
    url2 = "https://jsonplaceholder.typicode.com/users"
    arr = []
    my = {}

    for j in range(len(getfunc(url2))):
        for i in getfunc(url + str(getfunc(url2)[j]["id"])):
            mydict = {}
            mydict["task"] = i["title"]
            mydict["completed"] = i["completed"]
            ge = getfunc(url2)[j]
            mydict["username"] = ge["username"]
            arr.append(mydict)
        my[getfunc(url2)[j]["id"]] = arr
    with open("todo_all_employees.json", 'w') as f:
        json.dump(my, f)
