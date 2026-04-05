₿ BitWatch — Live Bitcoin Price Alert Bot

> 🚀 **Live Demo:** [Click here to try BitWatch on Telegram](https://t.me/EquitysharesBot)

A Telegram bot that tracks live Bitcoin prices in **INR** and **USD**, detects price changes automatically, and delivers real-time alerts straight to your phone — built completely from scratch in Python.

---

## What It Does

BitWatch connects to the CoinGecko API every hour, checks if the Bitcoin price has changed, and sends you a Telegram message if it has. You can also message the bot directly and it will reply with the current price, generate an AI powered Bitcoin fact using Groq's LLaMA 3, or start and stop automatic alerts — all from Telegram.

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
- 🔔 Automatic hourly price change detection and alerts
- 🤖 Interactive Telegram bot with 6 commands
- 🧠 AI generated Bitcoin facts powered by **Groq LLaMA 3**
- 🛡️ Duplicate alert prevention — one active alert per user
- 💬 Handles unknown messages gracefully
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
├── checker.py        # compares new price against last saved price
├── notifier.py       # sends Telegram alert when price changes
├── scheduler.py      # defines job() and hourly schedule
├── bot.py            # all Telegram bot commands and handlers
├── config.py         # reads secrets from environment variables
├── Procfile          # tells Railway which file to run
├── requirements.txt  # all Python dependencies
└── data/
    └── last_price.txt  # persists last known price between runs
```

Each file has a single responsibility. When I switched from web scraping to the CoinGecko API, I only changed `scraper.py` — nothing else broke. That's separation of concerns working in practice.

---

## How It Works

1. `main.py` starts two processes simultaneously using Python **threading**
2. The scheduler runs `job()` every hour in a **background daemon thread**
3. `job()` calls `scraper.py` to get the latest BTC price
4. `checker.py` compares it to the last saved price in `last_price.txt`
5. If the price changed — `notifier.py` sends a Telegram alert
6. Meanwhile the bot listens for commands in the **main thread** via polling

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

### 7. Create `config.py` in the project root
```python
import os

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
COINGECKO_KEY = os.environ.get("COINGECKO_KEY")
GROQ_KEY = os.environ.get("GROQ_KEY")
```

For local development set actual values directly. For deployment use environment variables.

> ⚠️ `config.py` is listed in `.gitignore` — never commit your secrets to GitHub.

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

## Key Engineering Decisions

**Separation of concerns** — each module has one job, making the codebase easy to extend and debug. Switching APIs required changing only one file.

**Threading over multiple processes** — running the scheduler and bot in the same process using threading avoids the complexity of process management while keeping both alive simultaneously.

**JobQueue for user alerts** — used python-telegram-bot's built-in JobQueue for per-user scheduled alerts instead of a second thread, keeping alert management within the async bot environment.

**CoinGecko Demo API** — chosen over the free tier because the free tier blocks cloud server IPs. The Demo API is designed for server use and works reliably on Railway.

**Environment variables for secrets** — API keys and tokens are never hardcoded. Locally stored in `config.py` via `.gitignore`, in production injected by Railway at runtime.

**Guard clauses for user safety** — duplicate `/alert` calls are rejected with a clear message. Unknown commands receive a helpful response instead of silence.

---

## Known Limitations

- Alert subscriptions reset if the server restarts — persistent alerts require a database
- Scheduler alerts go to one configured user — multi-user scheduler support requires storing chat IDs in a database
- No price history — planned for a future version

---

## Future Improvements

- Price threshold alerts — notify only when BTC crosses a user defined value
- Database integration for persistent multi-user alert subscriptions
- Support for multiple coins — ETH, SOL, BNB
- Proper logging using Python's `logging` module
- Simple web dashboard showing price history

---

## What I Learned Building This

- Consuming REST APIs and parsing JSON responses
- Separation of concerns and why it matters in practice
- Python threading and daemon threads
- JobQueue for async scheduled messaging
- UTF-8 encoding for Unicode currency symbols
- Environment variables and secrets management
- Cloud deployment and debugging production issues
- The difference between local and production behaviour

---

Built by **BALKRISHNA SAWANT** — self taught Python developer

⭐ Star this repo if you found it useful!
