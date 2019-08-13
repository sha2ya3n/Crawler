#!/usr/bin/env python
import requests

url = "google.com"

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

with open ("/home/sha2ya3n/Documents/Word-list/directories.txt", "r") as directories:
    for line in directories:
        word = line.strip()
        test_dir = url + "/" + word
        response = request(test_dir)
        if  response:
            print("[+] Directorie discovere >> " + test_dir)
