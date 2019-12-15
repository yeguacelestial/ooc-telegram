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
def fetch():
    os.system("python bot_wrapper.py")
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
        # Filtros
        tweet = tweet.replace("feminicidio", "perfectirijillo")
        tweet = tweet.replace("feminista", "unicornio")
        tweet = tweet.replace("violar", "extrañar")
        tweet = tweet.replace("violaste", "extrañaste")
        tweet = tweet.replace("violando", "rompiendo")
        tweet = tweet.replace("violador", "ingeniero")
        tweet = tweet.replace("violo", "extraño")
        tweet = tweet.replace("violó", "extrañó")
        tweet = tweet.replace("viole", "extrañe")
        tweet = tweet.replace("violé", "extrañé")
        tweet = tweet.replace("gorda", "hermosa")
        tweet = tweet.replace("cogiste", "conquistaste")
        tweet = tweet.replace("Mariana", "Tatiana")
        tweet = tweet.replace("mariana", "tatiana")
        tweet = tweet.replace("MARIANA", "TATIANA")
        tweet = tweet.replace("Miranda", "Sprite")
        tweet = tweet.replace("miranda", "joya de manzana")
        tweet = tweet.replace("MIRANDA", "DR PEPPER")
        tweet = tweet.replace("Marcela", "Magdalena")
        tweet = tweet.replace("marcela", "magdalena")
        tweet = tweet.replace("MARCELA", "MAGDALENA")
        tweet = tweet.replace("aborto", "trastorno")
        tweet = tweet.replace("Aborto", "VIH")
        tweet = tweet.replace("ABORTO", "SIDA")
        tweet = tweet.replace("niñas", "anguilas")
        tweet = tweet.replace("NIÑAS", "anguilas")
        tweet = tweet.replace("Niñas", "anguilas")
        tweet = tweet.replace("niñitas", "anguilitas")
        tweet = tweet.replace("NIÑITAS", "anguilitas")
        tweet = tweet.replace("BEBES", "DUENDES")
        tweet = tweet.replace("San Martin", "Don Martin")
        tweet = tweet.replace("Rubi", "Esmeralda")
        tweet = tweet.replace("rubi", "esmeralda")
        tweet = tweet.replace("RUBI", "ESMERALDA")
        tweet = tweet.replace("Rubí", "Esmeralda")
        tweet = tweet.replace("rubí", "esmeralda")
        tweet = tweet.replace("RUBÍ", "ESMERALDA")

        # Usernames
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
        tweet = tweet.replace("skinhell", "ImaPenguinxdd")
        tweet = tweet.replace("Rubidioo", "TheAsulio")

        if len(tweet) > 250:
            tweet = list(tweet)[:247]
            tweet.append("...")
            tweet = "".join(tweet)

        api.update_status(tweet)
        print("Tweet: {}".format(tweet))
        time.sleep(60*60)

    else:
        tweet = random.choice(mensajes_lista)

if __name__ == '__main__':
    fetch()