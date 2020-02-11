import os
import telegram
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()
update_id = None
bot_token = os.getenv('BOT_TOKEN')

# Twitter
consumer_key = os.getenv('TW_API_KEY')
consumer_secret_key = os.getenv('TW_API_SECRET_KEY')
access_token = os.getenv('TW_ACCESS_TOKEN')
access_secret_token = os.getenv('TW_ACCESS_SECRET_TOKEN')

def main():
    global update_id
    bot = telegram.Bot(bot_token)

    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    while True:
        try:
            echo(bot)
        except NetworkError as e:
            sleep(1)
        except Unauthorized as e:
            # The user has removed or blocked the bot.
            update_id += 1
        except:
            pass

    return bot

def echo(bot):
    #Echo the message the user sent
    global update_id

    # Request updates adter the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message.photo:
            try: 
                file = bot.getFile(update.message.photo[-1].file_id)
                print(f"PHOTO FILE: {file.file_path}")
                return file.file_path
            except Exception as e:
                print(f"Error: {e}")

        elif update.message:
            try:
                #reply = update.message.reply_text(update.message.text)
                print(update.message.text)
            except Exception as e:
                print(f"Error: {e}")

def tweet(consumer_key, consumer_secret_key, access_token, access_secret_token, img_url):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_secret_token)
    api = tweepy.API(auth)

    tweet_text = "TEST x2"

    # Img
    img = 'temp.jpg'
    request = requests.get(img_url, stream=True)
    if request.status_code == 200:
        with open(img, 'wb') as image:
            for chunk in request:
                image.write(chunk)


        status = api.update_with_media(img, tweet_text)
        #api.update_status(status=tweet_text)

if __name__ == '__main__':
    # b = main()
    # echo(b)
    tweet(consumer_key, consumer_secret_key, access_token, access_secret_token)