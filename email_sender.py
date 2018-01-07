import smtplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# set up the SMTP server
def send_email(file_path):
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(os.environ['GARAGE_EMAIL'], os.environ['GARAGE_EMAIL_PASSWORD'])

    recipient_list = ["akashsaluja@outlook.com"]

    for email in recipient_list:
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = "Hello, This is from Prayog Shala!"

        # setup the parameters of the message
        msg['From']=os.environ['GARAGE_EMAIL']
        msg['To']=email
        msg['Subject']="Dhvani Update: %s"%(time.strftime("%d/%m/%Y"))

        attachment = open(file_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % file_path)

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        msg.attach(part)

        # send the message via the server set up earlier.
        s.send_message(msg)
        