import tweepy
import time

auth = tweepy.OAuthHandler('W40cOHEY14OxIJHLuVkvjHAPp', 'P9GDIjMVUY0HVRvfR3EPU5nXEB6ePDp6LbsdyFPFe9eT1U2tpu')
auth.set_access_token('1230733636887957505-fOviHKag0gyaOvBisYJVRXqqgL8ry0',
                      'K1RI6QxeLxDvfJC6ksKadRR5AFu5gIXhMDsbBpIQNS7I8')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
user=api.me()
print(user)




def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

"""follow back bot
for follower in tweepy.Cursor(api.followers).items():
    if follower.name=="Mischievous":
        follower.follow()
    print(follower.name)"""

"""search bot
1 searches tweet
2 like tweet -favorite
3 retweet tweet-retweet"""

'''search_string='pushpa'
number_of_tweets=10

for tweet in tweepy.Cursor(api.search,search_string).items(number_of_tweets):
    try:
        tweet.favorite()
        print(tweet.text)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
'''

