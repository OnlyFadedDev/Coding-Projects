# Sending an email with Python

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = 'andrei@zerotomastery.to'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('testingemail4412@gmail.com', 'Basepassword')
  smtp.send_message(email)
  print('all good boss!')

