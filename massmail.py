import json
import smtplib
#import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time
from os.path import basename
import os

# MTA server info
smtp_server = "localhost"
port = 25
# context = ssl.create_default_context()

#real_sender_address = "harry@hz2.org"
#password = "--------" # password goes here (only needed if mail server requires login)

def sendEmail(receiver_address):
    email_fields_file = open("zoom.txt", "r")
    email_fields = json.loads(email_fields_file.read())
    email_fields_file.close()

    body_file = open(email_fields['body_file'], "r")
    body = body_file.read()
    # insert email address into variables in body template
    body = body.replace('{{email}}', receiver_address)
    body_file.close()
    
    msg = MIMEMultipart()
    msg['From'] = email_fields['from']
    msg['To'] = receiver_address
    msg['Subject'] = email_fields['subject']
    
    msg.attach(MIMEText(body, 'html'))
    if 'attachment' in email_fields:
        file_name = email_fields['attachment']
        file = open(file_name, "rb")
        part = MIMEApplication(
                file.read(),
                Name=basename(file_name)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file_name)
        msg.attach(part)

    # for attach in os.listdir("attachments"):
#         with open(os.path.join("attachments", attach), "rb") as file:
#             part = MIMEApplication(
#                 file.read(),
#                 Name=basename(attach)
#             )
#         # After the file is closed
#         part['Content-Disposition'] = 'attachment; filename="%s"' % basename(attach)
#         msg.attach(part)
    
    # Code to connect to mail server and send email
    #server = smtplib.SMTP(smtp_server, port)
    #server.starttls()

    #The server I was using did not require a login, but most mail servers will require one.
    #server.login("real_sender_address", password)
    #server.sendmail(email_fields['sender'], receiver_address, msg.as_string())
    print(msg.as_string())

receiversFile = open("receiversTest.txt", "r")
for address in receiversFile.readlines():
    sendEmail(address)
    print("sent email to " + address);
    time.sleep(6) #requires 5 but increased to 6 in case of any latency
