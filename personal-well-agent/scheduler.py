import schedule
import time

class WellnessScheduler:
    def __init__(self, agent, notifier):
        self.agent = agent
        self.notifier = notifier
        self.setup_schedule()

    def setup_schedule(self):
        schedule.every().day.at("07:00").do(self.send_wake_up_reminder)
        schedule.every(1).hours.do(self.send_water_reminder)
        schedule.every().day.at("06:30").do(self.send_morning_exercise_reminder)
        schedule.every().day.at("17:00").do(self.send_evening_exercise_reminder)

    def send_wake_up_reminder(self):
        message = self.agent.generate_reminder("Wake up and start your day with energy!")
        self.notifier.send_message(message)

    def send_water_reminder(self):
        message = self.agent.generate_reminder("Time to drink water and stay hydrated.")
        self.notifier.send_message(message)

    def send_morning_exercise_reminder(self):
        message = self.agent.generate_reminder("Good morning! It's time for your yoga session.")
        self.notifier.send_message(message)

    def send_evening_exercise_reminder(self):
        message = self.agent.generate_reminder("Let’s get moving! Time for your evening workout.")
        self.notifier.send_message(message)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(30)
