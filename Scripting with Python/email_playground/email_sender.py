import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'altin-osmanaj@hotmail.com'
email['to'] = 'altin.osmanaj@student.uni-pr.edu'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('altin-osmanaj@hotmail.com', 'Osm@naj321')
	smtp.send_message(email)
	print('All good boss!')