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

    def get_submissions(self, limit = 10):
        comments = []
        for submission in self.subreddit.hot(limit = limit):
            parsed_comment = {}
            parsed_comment['text'] = submission.title
            comments.append(parsed_comment)
        return comments
    
def main():

    reddit = redditClient()
    reddit.get_submissions(limit = 5)

if __name__ == "__main__":
    # call the main function
    main()
