#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for the given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyApp/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for entry in data:
            print(entry["data"]["title"])
    else:
        print(None)

