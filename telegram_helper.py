import os
from datetime import datetime
from twx.botapi import TelegramBot

bot = TelegramBot(os.environ["BOT_API_TOKEN"])
user_id = int(os.environ["USER_ID"])

def init_bot():
    global bot
    bot.update_bot_info().wait()
    print "Bot " + bot.username + " is ready!"

def send_message(message):
    global bot, user_id
    print bot.send_message(user_id, message).wait()

def get_updates(last_update_id=0):
    updates = bot.get_updates(offset=last_update_id).wait()
    return updates


if __name__ == "__main__":
    init_bot()
    get_updates()
