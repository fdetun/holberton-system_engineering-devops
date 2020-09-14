#!/usr/bin/python3
"""gathering from json and exprong ot to csv"""
import json
import requests


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

    for j in getfunc(url2):
        for i in getfunc(url + str(j["id"])):
            mydict = {}
            mydict["task"] = i["title"]
            mydict["completed"] = i["completed"]
            mydict["username"] = j["username"]
            arr.append(mydict)
        my[str(j["id"])] = arr
    with open("todo_all_employees.json", 'w') as f:
        json.dump(my, f)
