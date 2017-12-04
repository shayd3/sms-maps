from twilio.rest import Client
import os
# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_SID']
# Your Auth Token from twilio.com/console
auth_token  = os.environ['TWILIO_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12159832573",
    from_="+18564315999 ",
    body="Hi test!")

print(message.sid)
