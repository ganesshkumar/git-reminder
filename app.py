import logging, os
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from telegram_helper import send_message
from telegram_helper import get_updates
from contribution_checker import did_contribute
from message_processor import process_incoming_message

logging.basicConfig()
scheduler = None
bg_scheduler = None
last_contributed_date = None
skip_hours = [i for i in xrange(1,15)]

last_update_id = 0
if os.path.isfile('last_update_id.txt'):
    with open('last_update_id.txt', 'r') as f:
        last_update_id = int(f.read())
        f.close

def init_scheduler():
    global scheduler, bg_scheduler
    scheduler = BlockingScheduler()
    bg_scheduler = BackgroundScheduler()
    scheduler.daemonic = False

def start_checker():
    scheduler.add_job(notify_contribution, 'interval', seconds=60)
    bg_scheduler.add_job(check_for_updates, 'interval', seconds=5)
    try:
        bg_scheduler.start()
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

def notify_contribution():
    global skip_hours, last_contributed_date
    today = datetime.today()

    if today.time().minute is not 0 or today.time().hour in skip_hours:
        return

    # Will be reached only on the 0th minute of non skip hours
    if not did_contribute(today.date()):
        message = "You haven\'t contributed for the day";
    else:
        if last_contributed_date == today.date():
            print "Already send message for the day. Skipping."
            return
        last_contributed_date = today.date()
        message = "You have contributed for the day. Keep it up!"
    print "Sending message: " + message
    send_message(message)
    print '\n'

def check_for_updates():
    ''' Checking new incoming messages '''
    global last_update_id
    print datetime.today().time()
    print 'Last Update ' + str(last_update_id) + '\n'

    for update in get_updates(last_update_id):
        if update.update_id is not last_update_id:
            try:
                process_incoming_message(update.message.text)
            except:
                print update
                continue
            last_update_id = update.update_id + 1
            with open('last_update_id.txt', 'w') as f:
                f.write(str(last_update_id))
    return


if __name__ == "__main__":
    print "Staring git-checker"
    #init_scheduler()
    #start_checker()
    check_for_updates()
