# ₿ BitWatch — Live Bitcoin Price Alert Bot
 
> 🚀 **Live Demo:** [Click here to try BitWatch on Telegram](https://t.me/EquitysharesBot)
 
A Telegram bot that tracks live Bitcoin prices in **INR** and **USD**, sends automatic hourly alerts, and generates AI powered Bitcoin facts — built completely from scratch in Python and deployed 24/7 on Railway.
 
---
 
## What It Does
 
BitWatch runs two systems simultaneously using Python threading:
 
- A **background scheduler** that fetches and saves the latest BTC price every 6 hours silently in the background
- A **Telegram bot** that listens for commands and responds instantly
 
Users can check the current price anytime, subscribe to automatic hourly price updates, or get an AI generated Bitcoin fact — all directly from Telegram.
 
---
 
## Bot Commands
 
| Command | Description |
|---------|-------------|
| `/start` | Welcome message |
| `/check` | Get current Bitcoin price instantly |
| `/alert` | Start receiving automatic hourly price updates |
| `/stop_alert` | Stop automatic price updates |
| `/funfact` | Get an AI generated Bitcoin fun fact |
| `/services` | View all available commands |
 
---
 
## Features
 
- 📡 Live BTC price in both **INR** and **USD** via CoinGecko Demo API
- ⏰ Automatic hourly price updates via Telegram JobQueue
- 🧠 AI generated Bitcoin facts powered by **Groq LLaMA 3.3 70B**
- 🛡️ Duplicate alert prevention — one active alert per user
- 💬 Handles unknown messages gracefully
- 🔒 Secrets managed via environment variables — nothing hardcoded
- ☁️ Deployed 24/7 on **Railway**
 
---
 
## Tech Stack
 
| Layer | Technology |
|-------|------------|
| Language | Python 3.10 |
| Price Data | CoinGecko Demo API |
| Notifications | Telegram Bot API |
| Bot Framework | python-telegram-bot + JobQueue |
| AI Fun Facts | Groq API — LLaMA 3.3 70B |
| Scheduling | schedule + Python threading |
| Deployment | Railway |
 
---
 
## Project Architecture
 
```
BITWATCH/
│
├── main.py           # entry point — runs scheduler and bot simultaneously via threading
├── scraper.py        # fetches live BTC price from CoinGecko API
├── checker.py        # compares new price against last saved price, auto creates data folder
├── notifier.py       # sends Telegram alert messages
├── scheduler.py      # silently tracks price every 6 hours in background
├── bot.py            # all Telegram bot commands and handlers
├── config.py         # reads all secrets from environment variables
├── Procfile          # tells Railway which file to run
├── requirements.txt  # all Python dependencies
└── data/
    └── last_price.txt  # persists last known price between runs
```
 
---
 
## How It Works
 
```
main.py starts
    │
    ├── Thread 1 (background daemon)
    │   └── every 6 hours → scrape price → save to last_price.txt
    │
    └── Thread 2 (main thread)
        └── always listening → responds to /check /alert /funfact
```
 
1. `main.py` launches two processes simultaneously using Python **threading**
2. The scheduler silently fetches and saves BTC price every 6 hours
3. The bot listens for Telegram commands in the main thread
4. `/alert` uses **JobQueue** to send hourly price updates to subscribed users
5. `/check` fetches live price directly and replies instantly
6. `/funfact` calls Groq's LLaMA 3 API and returns a fresh AI generated fact
 
---
 
## Key Engineering Decisions
 
**Separation of concerns** — each file has one responsibility. When the API source changed, only `scraper.py` needed updating — nothing else broke.
 
**Threading over multiple processes** — scheduler and bot run in the same process using Python's `threading` module. The scheduler runs as a daemon thread so it automatically stops when the main thread exits.
 
**JobQueue for user alerts** — `/alert` uses python-telegram-bot's built-in JobQueue for per-user scheduled messages. This keeps alert management within the async bot environment and lets each user control their own subscription.
 
**Scheduler for background tracking only** — the scheduler silently saves price data every 6 hours without sending messages. This avoids duplicate notifications since JobQueue already handles user alerts.
 
**CoinGecko Demo API** — chosen over the free tier because the free tier blocks cloud server IPs. The Demo API is designed for server use and works reliably on Railway. At 4 calls per day we use 0.04% of the daily limit.
 
**Environment variables for secrets** — all API keys and tokens are read via `os.environ.get()`. Locally `config.py` reads from the environment. On Railway the dashboard injects values at runtime. No secrets ever committed to GitHub.
 
**Auto folder creation** — `checker.py` uses `os.makedirs("data", exist_ok=True)` to create the data folder automatically on Railway since `.gitignore` excludes it from the repo.
 
**Duplicate alert prevention** — `/alert` checks for existing JobQueue jobs before creating a new one, preventing users from receiving multiple notifications per hour.
 
---
 
## Setup & Installation
 
### 1. Clone the repo
```bash
git clone https://github.com/coder-bks/BitWatch.git
cd BitWatch
```
 
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
 
### 3. Create a Telegram Bot
- Search **BotFather** on Telegram
- Send `/newbot` and follow the steps
- Copy your **Bot Token**
 
### 4. Get your personal Chat ID
- Send any message to your bot on Telegram
- Visit `https://api.telegram.org/bot{TOKEN}/getUpdates`
- Find `"chat": {"id": ...}` — that number is your Chat ID
 
### 5. Get a free CoinGecko Demo API key
- Go to [coingecko.com/en/developers/dashboard](https://www.coingecko.com/en/developers/dashboard)
- Sign up and create a free Demo API key
 
### 6. Get a free Groq API key
- Go to [console.groq.com](https://console.groq.com)
- Sign up and create an API key
 
### 7. Set environment variables
Set these in your terminal or add directly to `config.py` for local development:
```
TOKEN=your_telegram_bot_token
CHAT_ID=your_personal_chat_id
COINGECKO_KEY=your_coingecko_demo_key
GROQ_KEY=your_groq_api_key
```
 
### 8. Run locally
```bash
python main.py
```
 
---
 
## Deployment on Railway
 
1. Push code to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Select the BitWatch repo
4. Add environment variables in Railway dashboard:
   - `TOKEN`
   - `CHAT_ID`
   - `COINGECKO_KEY`
   - `GROQ_KEY`
5. Railway reads the `Procfile` and deploys automatically
 
**Procfile:**
```
worker: python main.py
```
 
---
 
## Known Limitations
 
- Alert subscriptions reset if the server restarts — persistent alerts require a database
- Scheduler tracks price for one configured user — multi-user scheduler requires database storage
- CoinGecko Demo API caches responses for 30-60 seconds — `/check` reflects this
 
---
 
## Future Improvements
 
- Price threshold alerts — notify only when BTC crosses a user defined value
- Database integration for persistent multi-user subscriptions
- Support for multiple coins — ETH, SOL, BNB
- Proper logging using Python's `logging` module
- Simple web dashboard showing price history
 
---
 
## What I Learned Building This
 
- Consuming REST APIs and parsing JSON responses
- Separation of concerns and why it matters in practice
- Python threading and daemon threads
- JobQueue for async scheduled Telegram messaging
- UTF-8 encoding for Unicode currency symbols like ₹
- Environment variables and secrets management
- Debugging real production issues — API IP blocking, cloud file system differences
- The difference between local and production behaviour
 
---
 
Built by **Balkrishna Sawant** — self taught Python developer 
 
⭐ Star this repo if you found it useful!