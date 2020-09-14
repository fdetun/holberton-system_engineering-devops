#!/usr/bin/python3
"""gathering from json and exprong ot to csv"""
import csv
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
    for i in range(len(getfunc(url))):
        ge = getfunc(url)[i]
        arr.append([ge["userId"], uname, ge['completed'], ge['title']])
    with open(str(num) + '.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
        writer.writerows(arr)
