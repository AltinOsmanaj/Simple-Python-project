import tweepy
import time

consumer_key = 'uYBDdwWzKVlMq9ofGlZJoZ68z'
consumer_secret = 'IqDgaRuJMCbNd76hVCFHrr9oIYkRscjDajqZGcQlDjz9TSWat2'
access_token = '862039751171481600-j9YXYh6uPh0TE0mgMlsU5r92qw9VnX9'
access_token_secret = 'W5aya7CEuz5GqOuDXZN2vgAGWwJA51HjUWSvYL5LNJaop'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()

# print(user.name)
# print(user.screen_name)
# print(user.followers_count)

def limit_handler(coursor):
	try:
		while True:
			yield coursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)

search_string = 'python'
numbersOfTweets = 2

# Generous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
# 	#if follower.name == '':
# 	if follower.followers_count > 100:
# 		follower.follow()
# 		break


# Narcisist Bot
for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
	try:
		tweet.favorite()
		# tweet.retweet()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break