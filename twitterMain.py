from doctest import DocFileSuite
import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import TwitterFunction as tf
import TwitterInfo as ti

# Setsup for twitter
comsumer_key = ti.comsumer_key
comsumer_secret = ti.comsumer_secret
access_token = ti.access_token
access_token_secret = ti.access_token_secret
barrier_token = ti.barrier_token

# 트위터 API 생성, 
auth = tweepy.OAuthHandler(comsumer_key, comsumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

letter = ""

while(letter != "x"):
    explanationText = "Function Order list \n "
    letter = input("Please Type your order: ")
    userName = input("Type your user name: ")
    
    if letter == "t":
        tf.userTimeLineSearch(api, userName)
    
        





