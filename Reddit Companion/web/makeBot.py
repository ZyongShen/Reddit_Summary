import praw

class myBot:

    def __init__(self):
        self.reddit = praw.Reddit('bot1')
        self.subreddit = self.reddit.subreddit('UConn')
    
    def changeSub(self, name):
        self.subreddit = self.reddit.subreddit(name)

redditBot = myBot()
