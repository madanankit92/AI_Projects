# personal_wellness_agent/telegram_notifier.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

class TelegramNotifier:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")  # Your personal Telegram user ID

    def send_message(self, message):
        if not self.token or not self.chat_id:
            print("[❌] Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID")
            return

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message
        }
        try:
            response = requests.post(url, json=payload)
            print(f"[📩] Telegram message sent: {message}")
        except Exception as e:
            print(f"[❌] Failed to send Telegram message: {e}")
