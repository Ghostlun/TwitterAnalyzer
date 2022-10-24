from doctest import DocFileSuite
import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import json

def userTimeLineSearch(api, username):
    # tweetInfo contains tweepy data
    tweetInfo = api.user_timeline(username, tweet_mode = 'extended')

    print(tweetInfo)

    index = 0
    numbersArray = [] 
    textLineArray = []
    numOfLikesArray = []
    numOfRetweets = []
    createdAtArray = []
    tweetsAddressArray = []

    for i in tweetInfo:
        numbersArray.append(index)
        textLineArray.append(i.full_text) 
        numOfLikesArray.append(i.favorite_count) 
        numOfRetweets.append(i.retweet_count) 
        createdAtArray.append(i.created_at) 
        tweetsAddressArray.append(i.entities['urls']) 
        index = index + 1


    df = pd.DataFrame({"Index Number" : numbersArray, "Tweets Info" : textLineArray, "# of Likes" : numOfLikesArray,
                        "# of Retweets" : numOfRetweets, "createdAt" : createdAtArray, "tweetsAddressArray": tweetsAddressArray})
    df.to_csv('GeneratedData.csv', encoding='utf-8')