#!/usr/bin/env python

import requests

target_url = "google.com"

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


with open("/home/sha2ya3n/Documents/Word-list/Subdomains.txt", "r") as word_list:
    for line in word_list:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered Subdomains >> " + test_url)
