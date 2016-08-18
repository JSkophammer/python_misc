#!/usr/bin/env python
import tweepy, time
from random import randint
from keys import keys
from tkinter import *

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
filename = 'handles.txt'
message = ''

def add_handle(new_handle):
    handles = open(filename, 'a')
    handles.write(new_handle)
    handles.close()

def mass_tweet(message):
    tweet_list = open(filename, "r")
    handles = tweet_list.readlines()
    tweet_list.close()
    for name in handles:
        name = name.rstrip()
        m = name + " " + message
        s = api.update_status(m)
        nap = randint(1, 60)
        time.sleep(nap)

top = Tk()
top.title('Digital Lobbyist')
Label(top, text='Enter message:', bg='gray60', fg='black', font=('arial', 16,)).pack(side=TOP, expand=YES, fill=BOTH)
top.geometry('300x130')
entry1 = Entry(top, bg='gray90', fg='black')
entry1.pack(side=TOP)
button1 = Button(top, text='Send', command=(lambda: mass_tweet(entry1.get())))
button1.pack()
entry2 = Entry(top, bg='gray90', fg='black')
entry2.pack(side=TOP)
button2 = Button(top, text='Add Handle', command=(lambda: add_handle(entry2.get())))
button2.pack()

top.mainloop()