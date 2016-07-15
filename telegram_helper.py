import os
from datetime import datetime
from twx.botapi import TelegramBot

bot = TelegramBot(os.environ["BOT_ID"])
user_id = int(os.environ["USER_ID"])

def init_bot():
    global bot
    bot.update_bot_info().wait()
    print "Bot " + bot.username + " is ready!"

def send_message(message):
    global bot, user_id
    print bot.send_message(user_id, message).wait()

if __name__ == "__main__":
    init_bot()
    send_message("Hello World!")
