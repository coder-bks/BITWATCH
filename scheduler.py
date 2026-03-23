from scraper import scrapping
from notifier import notify
from checker import checking
import schedule
import time

def job():
    fresh_data = scrapping()          
    has_changed = checking(fresh_data)
    if has_changed:
        notify(f"Alert! Quote changed: {fresh_data}")  

schedule.every(1).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)