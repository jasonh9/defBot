#!/usr/bin/python

import praw

reddit = praw.Reddit('defBot') # name is relative to the name within the praw.ini file

subreddit = reddit.subreddit("worldnews") # subreddit to monitor

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
