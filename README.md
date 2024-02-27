## UIU Notice Bot

This is a Telegram bot that scrapes the notice section from the website of United International University (UIU) and sends the latest notices to users subscribed to the bot.

### Installation

1. Clone the repository.
2. Install dependencies using `pipenv`:
   ```bash
   pipenv install
3. Ensure you have a Firebase Realtime Database set up and obtain the `DATABASE_URL`.
4. Ensure you have a Telegram bot token (`TOKEN`).

### Configuration

1. Create a file named `TOKEN.py` and define your Telegram bot token as `TOKEN`.
2. Create a file named `firebase-adminsdk.json` and place your Firebase Admin SDK JSON key file in it.
3. Set your Firebase Realtime Database URL in `TOKEN.py` as `DATABASE_URL`.

### Usage

Run the bot using `python main.py`.

### Features

- **Start Command:** `/start` - Start the bot and subscribe to receive notices.
- **Help Command:** `/help` - Get help.
- **Automatic Update:** The bot automatically checks for new notices every 10 minutes.
- **Error Handling:** The bot handles errors gracefully.

### Database

The bot uses Firebase Realtime Database to store user information and notices.

### Dependencies

- `requests`
- `beautifulsoup4`
- `firebase-admin`
- `python-telegram-bot`

### How It Works

The bot scrapes the UIU website for notices, extracts the latest notice, and sends it to subscribed users via Telegram. It also provides commands for users to manually check for new notices or get help.


