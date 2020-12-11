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

fake_sender_address = "IT203 Notifications <IT203Notifications@napervillle203.org>" # Used for spoofing. Gmail is able to detect certain suspicious patterns, however.
#receiver_address = "hyzhou@stu.naperville203.org"

def sendEmail(receiver_address):
    subjectFile = open("zoom_subject.txt", "r")
    bodyFile = open("zoom_body.html", "r")
    msg = MIMEMultipart()
    msg['From'] = "IT203 Notifications <IT203Notifications@naperville203.org>"
    msg['To'] = receiver_address
    msg['Subject'] = subjectFile.read()
    body = bodyFile.read()
    subjectFile.close()
    bodyFile.close()
    
    # insert email address into variables in body template
    body = body.replace('{{email}}', receiver_address)
    
    msg.attach(MIMEText(body, 'html'))
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
    #server.sendmail(fake_sender_address, receiver_address, msg.as_string())
    print(msg.as_string())

receiversFile = open("receiversTest.txt", "r")
for address in receiversFile.readlines():
    sendEmail(address)
    print("sent email to " + address);
    time.sleep(6) #requires 5 but increased to 6 in case of any latency
