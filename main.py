from scheduler import job,schedule,time
from  bot import app
import threading

def run_scheduler():
    while True:
      schedule.run_pending()
      time.sleep(60)


def main():
# Launch scheduler in background thread
    thread = threading.Thread(target=run_scheduler)
    thread.daemon = True  # dies when main program dies
    thread.start()

# Bot polling runs in main thread
    app.run_polling()
if __name__ == "__main__":
    main()
