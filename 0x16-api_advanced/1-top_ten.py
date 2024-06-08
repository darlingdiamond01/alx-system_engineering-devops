#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API
    - If not valid subreddit, print none.
    """
req = requests.get(
    "https://www.reddit.com/r/{}hot.json".format(subreddit),
    headers={"User-Agent": "custom"},
    params={"limit": 10},
)

if reg.status_code == 200:
    for get_data in reg.json().get("data").get("children"):
        dat = get_data.get("data")
        title = dat.get("title")
        print(title)
else:
    print(none)
