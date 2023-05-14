 1 #!/usr/bin/python3
 2 """
 3 A function that queries the Reddit API and prints the titles of the first
 4 10 hot posts listed for a given subreddit.
 5 """
 6 import requests
 7
 8
 9 def top_ten(subreddit):
10     """
11     Queries the Reddit API and prints the titles of the first 10 hot posts
12     listed for the given subreddit.
13     """
14     url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
15     headers = {"User-Agent": "MyApp/1.0"}
16
17     response = requests.get(url, headers=headers, allow_redirects=False)
18     if response.status_code == 200:
19         data = response.json().get('data').get('children')
20         for entry in data:
21             print(entry.get('data').get('title'))
22     else:
23         print(None)

