from scraper import scrapping
from notifier import notify
from checker import checking
import schedule
import time


def job():
    try:
        fresh_data = scrapping()
        has_changed = checking(fresh_data)
        if has_changed:
            notify(f"Alert! Bitcoin price changed: {fresh_data}")
    except Exception as e:
        print(f"Job failed: {e}. Will retry next run.")

schedule.every(1).hours.do(job)


# IMPORTED IN THREADING
# while True:
#     schedule.run_pending()
#     time.sleep(60)

# TURNED to try and except AS API MAY FALL SOMETIMES
# def job():
#     fresh_data = scrapping()          
#     has_changed = checking(fresh_data)
#     if has_changed:
#         notify(f"Alert! Quote changed: {fresh_data}")  
 