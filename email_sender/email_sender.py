import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '---------@outlook.com'
email['to'] = '---------------'
email['subject'] = 'e-mail through python'

sender_email = '-------@outlook.com'
password = '---------'

email.set_content(html.substitute({'name':'NoOne'}), 'html')

# the below host is for outlook, there is different host for different servers

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, password)
    smtp.send_message(email)
    print('email sent')