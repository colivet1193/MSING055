import tweepy
import requests
from requests_oauthlib import OAuth1
import json
import csv
from datetime import datetime

#Credentials
consumer_key = ['consumer key 1','consumer key 1']
consumer_secret = ['consumer secret 1','consumer secret 2']
access_token = ['access toke 1','access toke 2']
access_token_secret = ['access token secret','access token secret']

tweetFile= open("tweetCollection_part3.csv", "w")
writer = csv.writer(tweetFile, delimiter=',')
line=["USER_NAME","TWEET_ID","TWEET_ID_STRING","CREATED_DATE","TEXT"]
writer.writerow(line)
tweetAccount=["LondonDLR","victorialine","centralline","wlooandcityline","piccadillyline"]
accountNo=0
i=0

#loop through the accounts
for account in tweetAccount:
    x=0
    accountNo+=1
    # OAuth process, using the keys and tokens
    if accountNo==1 or accountNo==15:
        print("--------------------------------------------")
        print("--------------------------------------------")
        print("Using the autentification method number "+str(i))
        print("--------------------------------------------")
        print("--------------------------------------------")
        
        auth = tweepy.OAuthHandler(consumer_key[0], consumer_secret[0])
        auth.set_access_token(access_token[0], access_token_secret[0])
        api = tweepy.API(auth)
        i+=1
    print("Started "+account)
	
	#Loop through the tweets
    for status in tweepy.Cursor(api.user_timeline, id=account).items(3242):      
        x+=1
        json_status = json.loads(json.dumps(status._json))
        userName=json_status["user"]["screen_name"]
        tweetId=json_status["id"]
        tweetIdStr=json_status["id_str"]
        tweetText=json_status["text"]
        datetime_object = datetime.strptime(json_status["created_at"], '%a %b %d %H:%M:%S %z %Y')
        line=[userName,tweetId,tweetIdStr,datetime_object,tweetText]
        writer.writerow(line)
		
		#Progress report
        if x%1000==0:
            print(x)
			
    print("Finished "+account)
    
tweetFile.close()
print("File closed")
