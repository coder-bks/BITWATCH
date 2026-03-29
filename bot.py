from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from config import TOKEN
from scraper import scrapping

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running with polling.")
async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fresh_data = scrapping()
    await update.message.reply_text(f'{fresh_data}')

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("check",check))

# IMPORTED IN THREADING
# app.run_polling()