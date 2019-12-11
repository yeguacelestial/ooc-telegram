# -*- coding: utf-8 -*-

import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
import os
from dotenv import load_dotenv
import sqlite3
import random
import time

load_dotenv()
update_id = None
bot_token = os.getenv('BOT_TOKEN')

#Config db
base = 'mensajes.db'
conexion = sqlite3.connect(base)
cursor = conexion.cursor()

#Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS msgs(
        mensaje VARCHAR(1000)
    )
''')

conexion.commit()

def main():
    # Run the bot
    global update_id
    bot = telegram.Bot(bot_token)

    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1

def echo(bot):
    #Echo the message the user sent
    global update_id

    # Request updates adter the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message: #Receive update without message
            # Add msg to db
            if update.message.text != None:
                conexion = sqlite3.connect("mensajes.db")
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO msgs (mensaje) VALUES (?)", (update.message.text, ) )
                print ("Added message to db: {}".format(update.message.text))
                conexion.commit()
                #tweet = random.choice(mensajes_lista)
                #print("Random msg: {}\n", tweet)
                #update.message.reply_text(tweet)

if __name__ == '__main__':
    main()