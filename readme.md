# ₿ BitWatch — Live Bitcoin Price Alert Bot

A Python-powered Telegram bot that tracks live Bitcoin prices in **INR** and **USD**, detects price changes, and delivers real-time alerts straight to your phone — automatically, every hour.

> Built from scratch as a portfolio project demonstrating Python backend development, REST API integration, Telegram Bot API, scheduling, threading, and cloud deployment.

---

## 🚀 Features

- 📡 **Live Price Tracking** — Fetches real-time BTC prices via CoinGecko API (no API key needed)
- 🔔 **Automatic Alerts** — Detects price changes and notifies you instantly on Telegram
- ⏰ **Hourly Scheduling** — Runs in the background every hour without any manual input
- 🤖 **Interactive Bot Commands** — Control everything directly from Telegram
- ☁️ **Cloud Deployed** — Running 24/7 on Railway

---

## 🤖 Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message and introduction |
| `/check` | Get the current Bitcoin price instantly |
| `/alert` | Start receiving automatic hourly price updates |
| `/stop_alert` | Stop automatic price updates |
| `/services` | View all available commands |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.10 |
| Price Data | CoinGecko REST API |
| Notifications | Telegram Bot API |
| Bot Framework | python-telegram-bot |
| Scheduling | schedule + threading |
| Deployment | Railway |

---

## 🏗️ Project Architecture

```
bitwatch/
│
├── main.py           # Entry point — runs scheduler + bot simultaneously via threading
├── scraper.py        # Fetches live BTC price from CoinGecko API
├── checker.py        # Compares new price against stored price, detects changes
├── notifier.py       # Sends Telegram alert when price changes
├── scheduler.py      # Defines job() and hourly schedule
├── bot.py            # Telegram bot commands and JobQueue handlers
├── config.py         # Stores TOKEN and CHAT_ID (never committed to git)
├── Procfile          # Railway deployment config
├── requirements.txt  # Python dependencies
└── data/
    └── last_price.txt  # Persists last known price between runs
```

> Each file has a single responsibility. This separation of concerns means swapping any layer (e.g. switching from CoinGecko to Binance API) requires changing only one file.

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/bitwatch.git
cd bitwatch
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a Telegram Bot
- Open Telegram and search for **BotFather**
- Send `/newbot` and follow the steps
- Copy the **Bot Token** you receive

### 4. Get your Chat ID
- Search for **userinfobot** on Telegram
- Send it a message — it will reply with your Chat ID

### 5. Configure credentials
Create a `config.py` file in the project root:
```python
TOKEN = "your_telegram_bot_token"
CHAT_ID = "your_telegram_chat_id"
```

> ⚠️ Never commit `config.py` to GitHub. It is listed in `.gitignore`.

### 6. Run locally
```bash
python main.py
```

---

## ☁️ Deployment (Railway)

1. Push your code to GitHub (without `config.py`)
2. Go to [railway.app](https://railway.app) and create a new project from your GitHub repo
3. Add environment variables in Railway dashboard:
   - `TOKEN` — your Telegram bot token
   - `CHAT_ID` — your Telegram chat ID
4. Railway auto-detects the `Procfile` and deploys automatically

**Procfile:**
```
worker: python main.py
```

---

## 💡 Key Engineering Decisions

- **Separation of concerns** — each module has one job, making the codebase easy to extend and test
- **Threading** — scheduler and Telegram bot run simultaneously in one process using Python's `threading` module
- **JobQueue** — used `python-telegram-bot`'s built-in JobQueue for async scheduled alerts instead of a second thread
- **CoinGecko API over scraping** — more reliable, no CAPTCHA issues, no authentication required
- **Pathlib over os.path** — cleaner cross-platform file handling
- **UTF-8 encoding** — all file operations explicitly use UTF-8 to handle currency symbols like ₹

---

## 📸 Demo

> Send `/check` to the bot and receive:
```
Bitcoin — INR: ₹74,50,000 | USD: $89,200
```

> Send `/alert` and get automatic updates every hour without lifting a finger.

---

## 👨‍💻 Author

Built by **Balkrishna Sawant** — a self-taught Python developer focused on backend systems, automation, and API integration.

---

## 📄 License

MIT License — free to use and modify.
