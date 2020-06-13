import tweepy 
import datetime 
consumer_key = 'vgkJyTRkaRN5DMAaMWC8kLHxt' 
consumer_secret = 'vOnvUNfJYcg8xJxdAr6qCDfSZytnLYnmpbKLvylOeZr7wxE6WJ' 
access_token = '824963554914729984-qfSABYELb502QHxP2Hp3fFT5wxIUqbM' 
access_token_secret = 'DSGOqWB6kI0l7BSVbxE8JYp0mVpUFc9MdZByjx9CnzsmE' 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
def publictweet():
    if datetime.date.today().weekday() == 0:
        tweettopublish = 'Hi everyone, today is Monday.   #Monday '
    if datetime.date.today().weekday() == 1:
        tweettopublish = 'Enjoy your Tuesday.  #Tuesday'
    if datetime.date.today().weekday() == 2:
        tweettopublish = 'Third week of the Week. #Wednesday'
    if datetime.date.today().weekday() == 3:
        tweettopublish = 'Thursday. I cannot wait for the Weekend'
    if datetime.date.today().weekday() == 4:
        tweettopublish = 'Friday...Finally'
    if datetime.date.today().weekday() == 5:
        tweettopublish = 'Weekend is approaching but no fun stuck with lockdown #lockdown'
        #status = api.update_with_media('pee.jpg')
        #api.update_status(status)
    if datetime.date.today().weekday() == 6:
        tweettopublish = 'Sunday morning...#Weekend #enjoy '
    api.update_status(tweettopublish)
    #api.update_status(status,'good morning')
    print(tweettopublish)
print(datetime.date.today().weekday())
publictweet()
