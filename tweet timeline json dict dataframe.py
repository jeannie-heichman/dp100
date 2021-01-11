import pandas as pd
import numpy as np
import tweepy
import json

consumer_key = "" #twitter app’s API Key
consumer_secret = "" #twitter app’s API secret Key
access_token = "" #twitter app’s Access token
access_token_secret = "" #twitter app’s access token secret



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


JenksTweets = auth_api.user_timeline(screen_name = 'PattyJenks', count = 600, include_rts = True, tweet_mode = 'extended') #api.user_timeline('JenksTweets')

my_list_of_dicts = []
for each_json_tweet in JenksTweets:
    my_list_of_dicts.append(each_json_tweet._json)

with open('tweet_json_jenks.txt', 'w') as file:
        file.write(json.dumps(my_list_of_dicts, indent=200))

my_demo_list = []
with open('tweet_json_jenks.txt', encoding='utf-8') as json_file:  
    all_data = json.load(json_file)
    for each_dictionary in all_data:
        tweet_id = each_dictionary['id']
        text = each_dictionary['full_text']
        favorite_count = each_dictionary['favorite_count']
        retweet_count = each_dictionary['retweet_count']
        created_at = each_dictionary['created_at']
        my_demo_list.append({'tweet_id': str(tweet_id),
                             'text': str(text),
                             'favorite_count': int(favorite_count),
                             'retweet_count': int(retweet_count),
                             'created_at': created_at,
                            })
        #print(my_demo_list)
        tweet_json = pd.DataFrame(my_demo_list, columns = 
                                  ['tweet_id', 'text', 
                                   'favorite_count', 'retweet_count', 
                                   'created_at'])
#tweet_json.createOrReplaceTempView("tweet_df")
        
display(tweet_json)