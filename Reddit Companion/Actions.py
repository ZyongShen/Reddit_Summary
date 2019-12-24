class Functions:

    def comment(self, submission, password=""):
        # submissions is a list of submission if user does not know which one
        # submission is the specific submission user wants to reply to
        defaultP = "12345"
        print("--------------------------------------------------------------")
        rep = str(input("What would you like to say?"))
        if password is defaultP:
            submission.reply(rep)


        
    def advanced(self, subreddit, keywords = []):
        submits = [submission for submission in subreddit.new(limit=10)] # take the five newest submissions
        criterias = [criteria.lower() for criteria in keywords] # break the criteria list in a list of strings
        results = []
        for sub in submits:
            curr = sub.title.lower()
            for criteria in criterias:
                if criteria in curr:
                    results.append(sub)
        return results
         
        
        
    def moreInfo(self, submissions):
        for submit in submissions:
            print("------------------------")
            print("Title: " + submit.title)
            print(submit.selftext)
            print("-------------------------")

    
    def overview(self, subreddit):
        submits = [submission for submission in subreddit.new(limit=5)]
        for submission in submits:
                print("-------------------------------------------------------")
                print("Title: ",submission.title)
                print("Author: ",submission.author)
                print("Upvotes: ",submission.ups)
                print("Downvotes: ",submission.downs)
                print("------------------------------------------------------")
        WR = str(input("Do you want to comment?"))
        if WR is "y" or WR is "yes" or WR is "YES":
            for i in range(0, len(submits)):
                print(str(i+1) + str(submits[i]))
            choice = str(input("Which one?"))
            choice = submits[int(choice)-1]
            password = str(input("What is the password?"))
            self.comment(choice, password)
        wantMore = str(input("Do you want more information?"))
        if wantMore == "YES" or wantMore == "y" or wantMore == "YES":
            self.moreInfo(submits)

    def getSummary(self, subreddit, type=""):
        if type == "new":
            submits = [submission for submission in subreddit.new(limit=5)]
            return submits
        elif type == "hot":
            submits = [submission for submission in subreddit.hot(limit=5)]
            return submits

    def printInfo(self, post):
        print("-----------------------------------")
        print("Title: " + str(post.title))
        print("Author: " + str(post.author))
        print("\nPost:")
        print(post.selftext)
        print(" ")
        print("Upvotes: " + str(post.ups) + " " + "Downvotes: " + str(post.downs))
        print("-----------------------------------")
