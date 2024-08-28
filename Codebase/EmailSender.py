# Sending an email with Python

import smtplib
from email.message import EmailMessage


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  
    email_address = 'testingemail4412@gmail.com'
    email_password = 'rioe ebcd nind ewok' # Need 2fa + app password for this script to work
    connection.login(email_address, email_password )
    connection.sendmail(from_addr=email_address, to_addrs='andrei@zerotomastery.io', 
    msg="subject:hi \n\n this is my message")
    connection.close()