#!/usr/bin/python

import praw
import re
from textblob import TextBlob



class redditComment(object):

    '''
    generic reddit class for sentiment analysis
    '''
    reddit = praw.Reddit('defbotboot')
    subreddit = reddit.subreddit("travel")

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
                parsed_comment['sentiment'] = self.get_comment_sentiment(submission.title)
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

        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
    
def main():

    reddit = redditComment()
    comments = reddit.get_submissions(limit = 100)

    positiveComments = [comment for comment in comments if comment['sentiment'] == 'positive']
    print("Positive comment percentage: {} %".format(100*len(positiveComments)/len(comments)))

    negativeComments = [comment for comment in comments if comment['sentiment'] == 'negative']
    print("Negative comment percentage: {} %".format(100*len(negativeComments)/len(comments)))

    neutralComments = [comment for comment in comments if comment['sentiment'] == 'neutral']
    print("Neutral comment percentage: {} %".format(100*len(neutralComments)/len(comments)))


    '''
    print the comments out for debugging purposes
    '''

    print("\n\nPositive Comments\n+++++++++++++++++++\n")
    for comment in positiveComments:
        print(comment['text'])


    print("\n\nNegative Comments\n+++++++++++++++++++\n")
    for comment in negativeComments:
        print(comment['text'])


if __name__ == "__main__":
    # call the main function
    main()
