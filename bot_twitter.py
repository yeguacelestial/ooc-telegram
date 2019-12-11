import tweepy
import time
import os
import random
import sqlite3
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv('TW_API_KEY')
consumer_secret_key = os.getenv('TW_API_SECRET_KEY')
access_token = os.getenv('TW_ACCESS_TOKEN')
access_secret_token = os.getenv('TW_ACCESS_SECRET_TOKEN')

# OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret_token)

# Creation of interface
api = tweepy.API(auth)

# Connect to db
base = 'mensajes.db'
conexion = sqlite3.connect(base)
cursor = conexion.cursor()

# Fetch msgs from db
while 1:
    cursor.execute("SELECT (mensaje) FROM msgs")
    mensajes = cursor.fetchall()
    mensajes_lista = []
    
    if len(api.user_timeline(id=api, count=1)) != 0:
        last_tweet = api.user_timeline(id=api, count=1)[0].text
    else:
        last_tweet = "None"

    for m in mensajes:
        mensajes_lista.append(str(m[0]))

    conexion.commit()

    timeline = api.user_timeline(screen_name='OutOfContextTlg', count=200, include_rts=False)
    tweets = []

    for tuit in timeline:
        tweets.append(tuit.text)

    tweet = random.choice(mensajes_lista)

    if (tweet != (last_tweet)) and (tweet not in tweets):
        tweet = tweet.replace("hombrecelestial", "yeguacelestial")
        tweet = tweet.replace("ComandoBurrito", "COMANDO_BURRITO")
        tweet = tweet.replace("VirgateGrunt", "FELG_STAR_")
        tweet = tweet.replace("fr0ppy", "BlackOXXO")
        tweet = tweet.replace("Ruben", "@laperraostia9")
        tweet = tweet.replace("Txocho", "Javsosa2000")
        tweet = tweet.replace("TOL0ACHE", "gersch_device")
        tweet = tweet.replace("Ricardo", "@ImaPenguinxdd")
        tweet = tweet.replace("Jack98fs", "FelipeS17871868")
        tweet = tweet.replace("brokeflounder", "Brokeflounder0")
        tweet = tweet.replace("Asulio", "TheAsulio")

        if len(tweet) > 250:
            tweet = list(tweet)[:247]
            tweet.append("...")
            tweet = "".join(tweet)

        api.update_status(tweet)
        print("Tweet: {}".format(tweet))
        time.sleep(60*60)

    else:
        tweet = random.choice(mensajes_lista)
