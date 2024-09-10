# Sending an email with Python also reading an html file and sending it out as normal text.

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('C:\VScode\Codebase\index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = 'andrei@zerotomastery.io'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(name= 'TinTin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('testingemail4412@gmail.com', 'privacy password, this won\'t work') # SMTPAuthenticationError: Need an app password from your google account.
  smtp.send_message(email)
  print('all good boss!')

