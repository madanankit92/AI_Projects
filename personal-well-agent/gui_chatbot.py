import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
from reminder_agent import ReminderAgent
from telegram_notifier import TelegramNotifier

class WellnessChatBot:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Personal Wellness Chatbot")
        self.window.geometry("600x500")

        self.agent = ReminderAgent()
        self.notifier = TelegramNotifier()

        # Chat log area
        self.chat_box = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, state='disabled', height=20)
        self.chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Input section
        input_frame = tk.Frame(self.window)
        input_frame.pack(padx=10, pady=5, fill=tk.X)

        self.entry_field = tk.Entry(input_frame)
        self.entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry_field.bind("<Return>", self.send_message)

        send_button = tk.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side=tk.RIGHT)

        # Welcome message
        self.update_chat("WellnessBot: Hi! You can type reminders or try /wake, /water, /yoga, /workout")

        self.window.mainloop()

    def send_message(self, event=None):
        user_input = self.entry_field.get().strip()
        if not user_input:
            return

        self.entry_field.delete(0, tk.END)
        self.update_chat(f"You: {user_input}")

        thread = Thread(target=self.respond_and_notify, args=(user_input,))
        thread.start()

    def respond_and_notify(self, prompt):
        command_map = {
            "/wake": "Wake up and start your day with energy!",
            "/water": "Time to drink water and stay hydrated.",
            "/yoga": "Good morning! It's time for your yoga session.",
            "/workout": "Let’s get moving! Time for your evening workout."
        }

        if prompt.lower() in command_map:
            prompt = command_map[prompt.lower()]

        response = self.agent.generate_reminder(prompt)
        self.update_chat(f"WellnessBot: {response}")
        self.notifier.send_message(response)

    def update_chat(self, message):
        self.chat_box.configure(state='normal')
        self.chat_box.insert(tk.END, message + "\n")
        self.chat_box.configure(state='disabled')
        self.chat_box.see(tk.END)

if __name__ == "__main__":
    WellnessChatBot()
