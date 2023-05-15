#!/usr/bin/python3
"""
This function queries the Reddit API and returns
a list containing the titles of all hot articles
for a given subreddit. If no results are found
for the given subreddit, the function should
return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot/.json?after={}".format
    (subreddit, after)
    headers = {"User-Agent": "custom"}

    data = requests.get(url, headers=headers, allow_redirects=False)
    if data.status_code == 200:
        after = data.json().get("data").get("after")
        data = data.json().get("data").get("children")
        for entry in data:
            hot_list.append(entry.get("date").get("title"))
        if after:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    return (None)
