import os
from twx.botapi import TelegramBot

bot = TelegramBot(os.environ["BOT_API_TOKEN"])
bot.update_bot_info().wait()

updates = bot.get_updates().wait()
print len(updates)
for update in updates:
    # Bot receives your message in this object. User id can be obtained from this update object.
    print(update)
