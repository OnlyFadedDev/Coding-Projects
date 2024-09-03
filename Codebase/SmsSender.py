# SMS With Python

from twilio.rest import Client
 
account_sid = '' # Secret
auth_token = '' # Secret
client = Client(account_sid, auth_token)
message = client.messages.create(
  messaging_service_sid='', # Secret
  body='Ahoy 👋',
  to='' # Secret
)
print(message.sid)



# Will try to make a new project with ntfy.sh instead because of simplicity.
# Does not use API keys or auth setup.



