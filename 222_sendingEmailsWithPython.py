import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = 'andrei@zerotomastery.io'
email['subject'] = "You won 1,000,000 dollars"

email.set_content('I am a Python Master')

#connect to the gmail account and compose a new message
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # "Extended Hello" https://stackoverflow.com/questions/72382443/what-is-smtp-server-ehlo-and-what-is-it-used-for 
    smtp.starttls() #encryption
    smtp.login('<name>@gmail.com' , '<password>')
    smtp.send_message(email)
    print('all good boss!')







