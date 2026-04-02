# ₿ BitWatch — Bitcoin Price Alert Bot

A Telegram bot that tracks live Bitcoin prices and sends you automatic alerts when the price changes. Built completely in Python as a portfolio project.

---

## What It Does

I built this because I wanted to learn how to work with real APIs, automate tasks, and deploy something that actually runs in production. BitWatch connects to the CoinGecko API every hour, checks if the Bitcoin price has changed, and sends a Telegram message if it has.

You can also message the bot directly and it will reply with the current price, generate an AI powered Bitcoin fact, or start and stop automatic alerts — all from Telegram.

---

## Features

- Live Bitcoin price in both INR and USD via CoinGecko API
- Automatic hourly price change detection
- Telegram alerts when price changes
- Interactive bot commands you can trigger anytime
- AI generated Bitcoin fun facts powered by Groq (LLaMA 3)
- Runs 24/7 on Railway cloud deployment

---

## Bot Commands

| Command | What it does |
|---------|-------------|
| `/start` | Welcome message |
| `/check` | Get current Bitcoin price right now |
| `/alert` | Start receiving automatic hourly price updates |
| `/stop_alert` | Stop automatic price updates |
| `/funfact` | Get an AI generated Bitcoin fun fact |
| `/services` | See all available commands |

---

## Tech Stack

- **Python 3.10** — main language
- **CoinGecko API** — live Bitcoin price data
- **Telegram Bot API** — sending and receiving messages
- **python-telegram-bot** — bot framework with JobQueue for scheduled messages
- **Groq API (LLaMA 3)** — AI generated fun facts
- **schedule + threading** — running scheduler and bot simultaneously
- **Railway** — cloud deployment

---

## Project Structure

```
BITWATCH/
│
├── main.py           # entry point, runs scheduler and bot together using threading
├── scraper.py        # fetches live BTC price from CoinGecko API
├── checker.py        # reads last saved price, compares with new price
├── notifier.py       # sends Telegram message when price changes
├── scheduler.py      # defines job() function and hourly schedule
├── bot.py            # all Telegram bot commands and handlers
├── config.py         # stores API keys and tokens (not uploaded to GitHub)
├── Procfile          # tells Railway which file to run
├── requirements.txt  # all Python dependencies
└── data/
    └── last_price.txt  # saves the last known price between runs
```

---

## How It Works

1. `main.py` starts two things simultaneously using Python threading
2. The scheduler runs `job()` every hour in a background thread
3. `job()` calls `scraper.py` to get the latest BTC price
4. `checker.py` compares it to the last saved price in `last_price.txt`
5. If the price changed, `notifier.py` sends a Telegram alert
6. Meanwhile the bot listens for commands in the main thread

I learned a lot about separation of concerns building this — each file has one job and doesn't know about the others. When I switched from web scraping to the CoinGecko API, I only had to change `scraper.py` and nothing else broke.

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/coker-bks/BitWatch.git
cd BitWatch
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a Telegram Bot
- Search for **BotFather** on Telegram
- Send `/newbot` and follow the steps
- Copy your bot token

### 4. Get your personal Chat ID
- Send any message to your bot on Telegram
- Visit `https://api.telegram.org/bot{TOKEN}/getUpdates`
- Find `"chat": {"id": ...}` in the response — that's your chat ID

### 5. Get a free Groq API key
- Go to [console.groq.com](https://console.groq.com)
- Sign up and create an API key

### 6. Create `config.py` in the project root
```python
TOKEN = "your_telegram_bot_token"
CHAT_ID = your_personal_chat_id
GROQ_KEY = "your_groq_api_key"
```

> `config.py` is listed in `.gitignore` and never uploaded to GitHub

### 7. Run locally
```bash
python main.py
```

---

## Deployment on Railway

1. Push code to GitHub (without `config.py`)
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Select the BitWatch repo
4. Add environment variables in Railway dashboard:
   - `TOKEN`
   - `CHAT_ID`
   - `GROQ_KEY`
5. Railway reads the `Procfile` and deploys automatically

**Procfile:**
```
worker: python main.py

```
🚀 **Live Demo:** [Click here to try BitWatch on Telegram](https://t.me/EquitysharesBot) 
---

## What I Learned Building This

- How to consume REST APIs and parse JSON responses
- How web scraping differs from API consumption and when to use each
- How to structure a project with separation of concerns so each module has one responsibility
- How threading works in Python and why it's needed when running two blocking processes
- How to use JobQueue in python-telegram-bot for async scheduled messages
- How to handle file encoding issues with Unicode characters like ₹
- How environment variables and `.gitignore` work for keeping secrets safe
- How to deploy a Python app to Railway and keep it running 24/7

---

## Future Improvements

- Add price threshold alerts — notify only when BTC crosses a specific value
- Store active chat IDs in a database for proper multi-user support
- Add more coins like ETH, SOL, BNB
- Build a simple web dashboard to view price history

---

Built by **BALRISHNA SAWANT** — self taught Python developer
