from scheduler import job,schedule,time
from  bot import app
import threading

def run_scheduler():
    while True:
      schedule.run_pending()
      time.sleep(60)


# Launch scheduler in background thread
def main():
    thread = threading.Thread(target=run_scheduler)
    thread.daemon = True  # dies when main program dies
    thread.start()

# Bot polling runs in main thread
    app.run_polling()
if __name__ == "__main__":
    main()
