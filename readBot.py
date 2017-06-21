#!/usr/bin/python

import praw
import re
from textblob import TextBlob



class redditClient(object):

    '''
    generic reddit class for sentiment analysis
    '''

    reddit = praw.Reddit('defbotboot')
    subreddit = reddit.subreddit("dogpictures")

    def clean_comment(self, comment):

        '''
        cleans the reddit comments up, remove links, special chars using regex statements
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", comment).split())

    def get_submissions(self, limit = 10):

        '''
        function to fetch reddit comments and parse them
        '''

        # create an empy list to store the parsed comments
        comments = []

        try:
            for submission in self.subreddit.hot(limit = limit):
                parsed_comment = {}
                parsed_comment['text'] = submission.title
                comments.append(parsed_comment)
            return comments
        except:
            print("Error with get_submisions")

    def get_comment_sentiment(self, comment):
        '''
        function to classify sentiment of passed reddit comment using textblob's sentiment analysis
        '''
        # create TextBlob object
        analysis = TextBlob(self.clean_comment(comment))


    
def main():

    reddit = redditClient()
    reddit.get_submissions(limit = 5)

if __name__ == "__main__":
    # call the main function
    main()
