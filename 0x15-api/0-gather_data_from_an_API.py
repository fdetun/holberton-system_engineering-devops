#!/usr/bin/python3
"""gathering from json"""
import requests
import sys


def getfunc(url):
    """ function to rturn json format from url"""
    r = requests.get(url)
    f = r.json()
    return f


if __name__ == "__main__":
    num = int(sys.argv[1])
    arr = []
    fal = 0
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"
    f = getfunc(url)
    for i in f:
        if i["userId"] == num:
            if i["completed"]:
                arr.append(i["title"])
            else:
                fal += 1
    f2 = getfunc(url2)
    for j in f2:
        if j["id"] == num:
            nam = j["name"]
    print("Employee {} is done with tasks({}/{}):".format(nam, len(arr), len(arr) + fal))
    for n in arr:
        print("\t{} ".format(n))
