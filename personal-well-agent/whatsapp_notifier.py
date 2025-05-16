# # personal_wellness_agent/whatsapp_notifier.py
# from twilio.rest import Client
# import os

# class WhatsAppNotifier:
#     def __init__(self):
#         self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
#         self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
#         self.from_whatsapp_number = 'whatsapp:8886052712' 
#         self.to_whatsapp_number = os.getenv('MY_WHATSAPP_NUMBER')
#         self.client = Client(self.account_sid, self.auth_token)

#     def send_message(self, message):
#         try:
#             self.client.messages.create(
#                 body=message,
#                 from_=self.from_whatsapp_number,
#                 to=self.to_whatsapp_number
#             )
#             print(f"[📩] WhatsApp message sent: {message}")
#         except Exception as e:
#             print(f"[❌] Failed to send WhatsApp message: {e}")