import requests
import bs4
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1

auth_params = {
    'app_key':'MljVzwf8nznqNPud49uAKEoqN',
    'app_secret':'SUz5Igo2Xgo8dCiJLtnORcUUOdpAu1VzJaZnpZ0eSJlY1OIxXF',
    'oauth_token':'784441002622750720-AsoD6p0YmsxFqzZjzZfaI11cz7Z6JVy',
    'oauth_token_secret':'BlNyzs0rTmsD9Jfk3S7stT8OVDPfNP5OEB9uDKN8uAbho'
}

# Creating an OAuth Client connection
auth = OAuth1 (
    auth_params['app_key'],
    auth_params['app_secret'],
    auth_params['oauth_token'],
    auth_params['oauth_token_secret']
)

url_rest = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# getting rid of retweets in the extraction results and filtering all replies to the tweet often uncessary for the analysis
q = 'siddharth_21998' # Twitter handle of Amazon India

# count : no of tweets to be retrieved per one call and parameters according to twitter API
params = {'screen_name': q, 'count': 2,'tweet_mode' :  'extended', 'extended_entities':1}
results = requests.get(url_rest, params=params, auth=auth)


tweets = results.json()

messages = [BeautifulSoup(tweet['full_text'], 'html5lib').get_text() for tweet in tweets]
print (messages,tweets[1]['retweet_count'])
