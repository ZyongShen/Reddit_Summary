import praw
import pdb
import re
import os
import random
from Actions import Functions

class Companion:
    def __init__(self, sub):
        self.subreddit = sub
        self.favorites = [] # store this in a text file
    
    def addFavorites(self, submission):
        pass

    def getFavorites(self):
        if len(self.favorites) == 0:
            print("No favorites")
    
    def callTask(self, option):
        if option == 1:
            Functions.overview(self, self.subreddit)
        elif option == 2:
            self.getFavorites()
        elif option == 3:
            subms = self.subreddit.new(limit=20)
            Functions.advanced(self, subms)
    
    def startup(self):

        print("1: Basic overview")
        print("2: Get Favorites")
        print("3: Advanced Search")
        choice = int(input("What would you like to do?"))
        self.callTask(choice)

    def main(self):
        while True:
            self.startup()



        
    

"""
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("raptors lets get it", submission.title, re.IGNORECASE):
            submission.reply("#insanity in toronto")
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)
"""     
        
