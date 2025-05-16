# personal_wellness_agent/main.py
from scheduler import WellnessScheduler
from reminder_agent import ReminderAgent
from telegram_notifier import TelegramNotifier
from threading import Thread
import gui_chatbot  # GUI chatbot interface
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# ✅ Required environment variables for OpenAI + Telegram
required_env = ["OPENAI_API_KEY", "TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID"]
for key in required_env:
    if not os.getenv(key):
        raise EnvironmentError(f"Missing required environment variable: {key}")

# Initialize the agent and services
agent = ReminderAgent()
notifier = TelegramNotifier()
scheduler = WellnessScheduler(agent, notifier)

# Run the chatbot GUI in a separate thread
def run_gui():
    gui_chatbot.WellnessChatBot()

gui_thread = Thread(target=run_gui)
gui_thread.start()

# Run the reminder scheduler loop
print("[✅] Personal Wellness Agent is running...")
scheduler.run()


