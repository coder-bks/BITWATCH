from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from config import TOKEN
from scraper import scrapping

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Heyy, Welcome. How can I help You? type /services to view all the services.")
async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fresh_data = scrapping()
    await update.message.reply_text(f'{fresh_data}')

async def send_alert(context: ContextTypes.DEFAULT_TYPE):
    fresh_data = scrapping()
    await context.bot.send_message(chat_id=context.job.chat_id, text=fresh_data)

async def alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.job_queue.run_repeating(
        send_alert, 
        interval=3600, 
        chat_id=update.effective_chat.id, 
        name="price_alert"
    )
    await update.message.reply_text("Alert service started! You'll get updates every hour.")

async def stop_alert(update, context):
    jobs = context.job_queue.get_jobs_by_name("price_alert")
    for job in jobs:
        job.schedule_removal()
    await update.message.reply_text("Alert service stopped!")



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text("/start - Greetings /check - to check current bitcoin price /alert - to start automatic price view service /stop_alert - to stop automatic price view service")


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("check",check))
app.add_handler(CommandHandler("alert",alert))
app.add_handler(CommandHandler("stop_alert",stop_alert))
app.add_handler(CommandHandler("help_command",services))


# IMPORTED IN THREADING
# app.run_polling()

#add package python-telegram-bot[job-queue]