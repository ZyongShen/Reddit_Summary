import praw
import pdb
import re
import os
import random
from Actions import Functions as func
import PySimpleGUI as sg

class Application:

    def __init__(self):
        self.sub = None
        self.makebot()
        self.makeMain()

    def makebot(self, subR='UConn'):
        reddit = praw.Reddit('bot1')
        subreddit = reddit.subreddit(subR)
        self.sub = subreddit

    def makeMain(self): # make the physical gui

        sg.ChangeLookAndFeel('LightGreen')
        sg.SetOptions(element_padding=(0,0))

        # ---Menu Definitions--- #
        menu_def = [
            ['File', ['Save', 'Exit']], 
            ['Reddit', ['Subreddit', 'Summary',['New', 'Hot'], 'Advanced']], 
            ['Clear',['All',]], 
            ['Help', ['About', 'Instructions', ]]
            ]

        # ---GUI Definition--- #
        layout = [
            [sg.Menu(menu_def, )],
            [sg.Output(size=(100, 40), key='_output_')]
        ]

        window = sg.Window("Window-like program", layout, default_element_size=(12,1), auto_size_text = False, auto_size_buttons = False, default_button_element_size = (12,1))

        # ---Popup input window--- #

        # ---Loop and Process button menu choices--- #
        while True:
            event, values = window.read()
            if event == None or event == 'Exit':
                break
            # --- Process menu choices ---#
            if event == 'About':
                sg.popup('Reddit Companion', 'Version 0.01')
            elif event == 'Instructions':
                window.FindElement('_output_').Update('Instructions \n Click on Reddit tab to see options \n Click on Subreddit to change the subreddit, the default is "UConn" \n Click on Overview to get quick summaries \n Click on Advanced to create a specific search')
            elif event == 'All':
                window.FindElement('_output_').Update('')
            elif event == 'New':
                window.FindElement('_output_').Update('')
                newest = func.getSummary(self, self.sub, "new")
                for post in newest:
                    func.printInfo(self, post)
            elif event == 'Hot':
                window.FindElement('_output_').Update('')
                hottest = func.getSummary(self, self.sub, "hot")
                for post in hottest:
                    func.printInfo(self, post)
            elif event == "Advanced":
                text = sg.PopupGetText('Only separate words with spaces.', 'Search Criteria')
                if text != None:
                    window.FindElement('_output_').Update('')
                    inputs = str(text).split()
                    results = func.advanced(self, self.sub, inputs)
                if results != None:
                    for post in results:
                        func.printInfo(self, post)
            elif event == 'Subreddit':
                subR = sg.PopupGetText('Subreddit?', 'Change Subreddit')
                self.makebot(subR)


        window.close()



redditProg = Application()
