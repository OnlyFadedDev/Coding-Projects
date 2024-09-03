# SMS With Python

from twilio.rest import Client

account_sid = 'AC1e7098980c53b296e851478742bbd1d8'
auth_token = '3e6ce64f503ca4aeb7b02da1e7312d82'
client = Client(account_sid, auth_token)
message = client.messages.create(
  messaging_service_sid='MG2f45a2737d1e4d1fa696b4558fb4ab22',
  body='Ahoy 👋',
  to=''
)
print(message.sid)



# Will try to make a new project with https://ntfy.sh instead because of simplicity.
# Does not use API keys or auth setup.



