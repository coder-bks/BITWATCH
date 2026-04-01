from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from config import TOKEN
from scraper import scrapping
from config import GROQ_KEY
from groq import Groq
import asyncio

client = Groq(api_key=GROQ_KEY)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Heyy, Welcome to BitWatch Services. How can I help You? type /services to view all the services.")
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


async def funfact(update, context):
    loop = asyncio.get_event_loop()

    response = await loop.run_in_executor(
        None,
        lambda: client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "user",
                "content": "Give a interesting Bitcoin fact or sarcastic joke in 1 sentences."
            }]
        )
    )

    text = response.choices[0].message.content

    await update.message.reply_text(text)


async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text(
    "🤖 *Bitcoin Alert Bot BITWATCH — Commands*\n\n"
    "/start — Welcome message\n"
    "/check — Get current Bitcoin price\n"
    "/alert — Start hourly price alerts\n"
    "/stop\\_alert — Stop price alerts\n"
    "/services — Show this menu",
    parse_mode="Markdown"
)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("check",check))
app.add_handler(CommandHandler("alert",alert))
app.add_handler(CommandHandler("stop_alert",stop_alert))
app.add_handler(CommandHandler("services",services))
app.add_handler(CommandHandler("funfact", funfact))


# IMPORTED IN THREADING
# app.run_polling()

