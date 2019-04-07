import tweepy 

# Fill the X's with the credentials obtained by 
# following the above mentioned procedure. 
consumer_key = "MljVzwf8nznqNPud49uAKEoqN"
consumer_secret = "SUz5Igo2Xgo8dCiJLtnORcUUOdpAu1VzJaZnpZ0eSJlY1OIxXF"
access_key = "784441002622750720-AsoD6p0YmsxFqzZjzZfaI11cz7Z6JVy"
access_secret = "BlNyzs0rTmsD9Jfk3S7stT8OVDPfNP5OEB9uDKN8uAbho"

# Function to extract tweets 
def get_tweets(username): 
		
		# Authorization to consumer key and consumer secret 
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

		# Access to user's access key and access secret 
		auth.set_access_token(access_key, access_secret) 

		# Calling api 
		api = tweepy.API(auth) 

		# 200 tweets to be extracted 
		number_of_tweets=1
		tweets = api.user_timeline(screen_name=username) 

		# Empty Array 
		# tmp=[] 

		# # create array of tweet information: username, 
		# # tweet id, date/time, text 
		# tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
		# for j in tweets_for_csv: 

		# 	# Appending tweets to the empty array tmp 
		# 	tmp.append(j) 

		# # Printing the tweets 
		# print(tmp) 
		print tweets


# Driver code 
if __name__ == '__main__': 

	# Here goes the twitter handle for the user 
	# whose tweets are to be extracted. 
	get_tweets("midasIIITD") 
