#customize the emails per individual

#https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/
#https://docs.python.org/3/library/string.html


import smtplib
from email.message import EmailMessage
from string import Template 
from pathlib from Path

html = Path('index.html').read_text()


email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = 'andrei@zerotomastery.io'
email['subject'] = "You won 1,000,000 dollars"

#email.set_content('I am a Python Master') is updated into:
email.set_content(html.substitute({name='Tintin'}), 'html')

#connect to the gmail account and compose a new message
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # "Extended Hello" https://stackoverflow.com/questions/72382443/what-is-smtp-server-ehlo-and-what-is-it-used-for 
    smtp.starttls() #encryption
    smtp.login('<name>@gmail.com' , '<password>')
    smtp.send_message(email)
    print('all good boss!')
