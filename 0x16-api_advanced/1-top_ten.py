#!/usr/bin/python3
"""A function that queries the Reddit API
prints the titles of the first 10 hot posts 
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit =10".format(subreddit)
    headers = {"User-Agent": "MyApp/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for entry in date:
            print(entry.get('data'.get('title'))
    else:
        print(None)
