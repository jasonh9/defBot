#!/usr/bin/python

import praw
import re
from textblob import TextBlob



class redditClient(object):

    '''
    Generic reddit class for sentiment analysis
    '''

    reddit = praw.Reddit('defbotboot')
    subreddit = reddit.subreddit("dogpictures")

    def get_submissions(self):
        for submission in self.subreddit.hot(limit=5):
            print(submission.title)
    
def main():

    reddit = redditClient()
    reddit.get_submissions()

if __name__ == "__main__":
    # call the main function
    main()
