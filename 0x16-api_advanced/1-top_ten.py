#!/bin/usr/python3

import requests

"""
A function that queries the Reddit API and 
prints the titles of the first 10 hot posts 
"""

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":"MyApp/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for entry in data:
            print(entry.get('data').get('title'))
        else:
            print(None)
