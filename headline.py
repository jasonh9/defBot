#!/usr/bin/python

import praw
import re
from textblob import TextBlob


class redditHeadline(object):

    '''
    generic reddit class for sentiment analysis
    '''
    reddit = praw.Reddit('defbotboot')
    subreddit = reddit.subreddit("travel")

    def clean_headline(self, headline):

        '''
        cleans the reddit headlines up, remove links, special chars using regex statements
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", headline).split())

    def get_submissions(self, limit = 10):

        '''
        function to fetch reddit headlines and parse them
        '''
        # create an empy list to store the parsed headlines
        headlines = []

        try:
            for submission in self.subreddit.hot(limit = limit):
                parsed_headline = {}
                parsed_headline['text'] = submission.title
                parsed_headline['sentiment'] = self.get_headline_sentiment(submission.title)
                headlines.append(parsed_headline)
            return headlines
        except:
            print("Error with get_submisions")

    def get_headline_sentiment(self, headline):
        '''
        function to classify sentiment of passed reddit headline using textblob's sentiment analysis
        '''
        # create TextBlob object
        analysis = TextBlob(self.clean_headline(headline))

        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
    
def main():
    
    reddit = redditHeadline()
    headlines = reddit.get_submissions(limit = 50)

    positiveHeadlines = [headline for headline in headlines if headline['sentiment'] == 'positive']
    print("Positive headline percentage: {} %".format(100*len(positiveHeadlines)/len(headlines)))

    negativeHeadlines = [headline for headline in headlines if headline['sentiment'] == 'negative']
    print("Negative headline percentage: {} %".format(100*len(negativeHeadlines)/len(headlines)))

    neutralHeadlines = [headline for headline in headlines if headline['sentiment'] == 'neutral']
    print("Neutral headline percentage: {} %".format(100*len(neutralHeadlines)/len(headlines)))

    print("\n\nPositive Headlines\n+++++++++++++++++++\n")
    for headline in positiveHeadlines:
        print(headline['text'])


    print("\n\nNegative Headlines\n+++++++++++++++++++\n")
    for headline in negativeHeadlines:
        print(headline['text'])


if __name__ == "__main__":
    # call the main function
    main()
