#!/usr/bin/python

import praw
import pdb
import re
import os

class redditReply(object):

    reddit = praw.Reddit('defbotboot')
    subreddit = reddit.subreddit("rsab")

    def reply_comment(self, limit):

        if not os.path.isfile("reply_text.txt"):
            reply_post = []
        
        else:
        
            # use with so we don't have to try, catch to debug errors
            with open("reply_text.txt", "r") as f:
                # read the file and split on newline
                reply_post = f.read()
                reply_post = reply_post.split("\n")
                # if file contains empty elements, remove them
                reply_post = list(filter(None, reply_post))
        
            for submission in subreddit.comments(limit = limit):
                if submission.id not in reply_post:
                    if re.search("!defbot rate comments", submission.body, re.IGNORECASE):
                        # reply to the post
                        submission.reply("Insert Sentiment Analysis here")
                        print("Bot replying to : ", submission.body)
        
                        reply_post.append(submission.id)
        with open("reply_post.txt", "w") as f:
            for post_id in reply_post:
                f.write(post_id + "\n")

def main():
    reddit = redditReply()
    reply = reddit.reply_comment(limit = 25)


if __name__ == "__main__":
    main()
    



