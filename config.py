import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
BOT_TOKEN = "8954780204:AAFLqtQgH55Bl-x8VxKXAzL8VgpztphOVNs"

# Web Server Configuration
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://yourdomain.com")
WEBHOOK_PATH = "/webhook"
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "your_secret_key")

# Server Configuration
HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", 8080))

# Database Configuration (optional)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///bot.db")

# Debug Mode
DEBUG = os.getenv("DEBUG", "False") == "True"
