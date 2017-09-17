from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

t = Twython(consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)

results = t.search(q="@MyFlightGenie", )
all_tweets = results['statuses'] 

for tweet in all_tweets:
    print(tweet['text'])

 
