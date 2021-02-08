import tweepy
import time
import random

consumer_key = 'XXX'
consumer_secret = 'XXX'
key = 'XXX'
secret = 'XXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


def tweetarBBB():
    if time.localtime().tm_min == 30 or time.localtime().tm_min == 0:
        api.update_status(tweetar() + random_line('palavroes.txt').lower() + '\n' + 'Dia ' + day + '/' + mes + '/' + ano + ', ' + hours())
    return time.sleep(60)

def tweetar():
    total_tweets = ['O BBB eh uma ', 'O BBB eh uma grande ', 'O BBB eh igual a uma ', 'O BBB eh tao ruim que parece ', 'Odeio tanto o BBB que preferia ver um ']
    tweet_random = total_tweets[random.randint(0,len(total_tweets)-1)]
    return tweet_random

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

hour_count = time.localtime().tm_hour

def hours():
        if time.localtime().tm_hour < 10:
            hour = '0' + str(hour_count)
        else:
            hour = str(hour_count)
        if time.localtime().tm_min < 10:
            minute = '0' + str(time.localtime().tm_min)
        else:
            minute = str(time.localtime().tm_min)
        horas = hour + ':' + minute
        return horas

while True:
    mes = str(time.localtime().tm_mon)
    ano = str(time.localtime().tm_year)
    day = str(time.localtime().tm_mday)
    tweetarBBB()
