[![Code Climate](https://codeclimate.com/github/ganesshkumar/git-reminder/badges/gpa.svg)](https://codeclimate.com/github/ganesshkumar/git-reminder)

# Git Reminder
> A telegram bot that will remind you to contribute code to Github everyday

<div>
  <img src="http://i.imgur.com/3GJYeG8.png" height="30%" width="30%">
  <img src="http://i.imgur.com/xEfxrqb.png" height="30%" width="30%">
</div>

## What does it do?

* Your Github contribution will be parsed from the URL `https://github.com/users/<user_name>/contributions`(Your contributions to private repos may or maynot be counted depending on your settings)
* Once a contribution success message is sent, you won't receive any more messages for that day
* If you haven't contributed for the day, you will be notified every one hour. There is a **skip_hours** [array](https://github.com/ganesshkumar/git-reminder/blob/master/app.py#L8) in `app.py`. Configure it to choose the hours during which you don't want to receive notification.

## To DO

* [ ] A collection of funky messages to choose from (instead of boring the user with the same content again and again)
* [ ] Ask the bot not to disturb for the rest of the day
* [x] Dockerize
* [ ] One Bot for all the users, instead of each user creating a bot

## Usage

### 1. Create a Telegram Bot

* Install Telegram and add the bot `@BotFather` to your contacts
* Text `/help` to @BotFather. You will create your bot over a chat and obtain the `HTTP API Token`

### 2. Download the code
Clone or fork this repo to your machine and install the dependencies.
```
pip install -r requirements.txt
```

### 3. Environment Variables

* `BOT_API_TOKEN`: This is the HTTP API Token you obtained when creating the bot
* `USER_ID`: Once you have created a Telegram Bot, send a message to the bot and obtain your userId when the bot receives your userId
* `GITHUB_USER_NAME`: your github username

Use the following script to get your userId
``` python
# Send a message to your bot and run this python script
from twx.botapi import TelegramBot

bot = TelegramBot(os.environ["BOT_API_TOKEN"])
bot.update_bot_info().wait()

updates = bot.get_updates().wait()
for update in updates:
    # Bot receives your message in this object. User id can be obtained from this update object.
    print(update)
```

### 4. Run the program
```
python app.py
```

### Docker Container
Instead of step 2, 3 and 4, you can use docker container to run the application. The [Docker Image](https://hub.docker.com/r/ganesshkumar/git-reminder/) has been published in Dockerhub. 

**Pull the image**
```
docker pull ganesshkumar/git-reminder
```

**Running the container**
```
docker run -e "BOT_API_TOKEN=<telegram_bot_api_token>" \
           -e "USER_ID=<telegram_user_id>" \
           -e "GITHUB_USER_NAME=<github_username>" \
           -e "PYTHONUNBUFFERED=0" \  # to force stdin, stdout to print to console without buffering 
           -e "TZ=Asia/Kolkata" \     # set the timezone else timezone will be UTC
           --name git-reminder  \
           ganesshkumar/git-reminder
```
