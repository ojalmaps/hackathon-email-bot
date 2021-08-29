# import smtplib   # Python’s built-in module for sending email


import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv


sender_email = 'knowledgef97@gmail.com'
receiver_email = 'ojalmaps@gmail.com'
# subject = "Get Dinner tonight"
# body = "Eat at 7pm ASAP"
password = 'passion@123'

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#     smtp.login(sender_email,EMAIL_PASSWORD)
# smtp.sendmail(sender_email, receiver_email,msg)


subject = "Subject: GraceHacks UCSC Female and Non-Binary Hackathon Sponsorship"
body ="""
Hi , 
I help organize GraceHacks, an annual, beginner-friendly student-led hackathon for women and non-binary students in tech taking place at the University of California Santa Cruz. We hope to have 100+ women and non-binary students learn new skills in a supportive, low-pressure environment.


What is GraceHacks?
GraceHacks is a 12-hour hackathon at the University of California Santa Cruz for female and non-binary students and includes a day full of hacking, learning and using new technologies.
The aim of GraceHacks is to foster a welcoming and supportive hackathon environment for womxn and non-binary students. GraceHacks strives to empower these underrepresented groups and ensure that they have the confidence to create without inherent bias or sexism and to encourage their passion to excel in STEM fields.
GraceHacks successfully held its first virtual hackathon in October 2020 with over 100 women/non-binary attendees.

What we’re looking for:
We’re currently looking for sponsors to make this year’s hackathon possible. We hope to hold this year’s hackathon during November at the University of California Santa Cruz. If COVID-19 situations do not allow an in-person event, we will be holding our event virtually.


I'm wondering if you think {name} would be interested in sponsoring. It would be great to have {name} at GraceHacks and would encourage women and non-binary college students to pursue STEM careers.
I have attached the sponsorship packet to this email. Please let me know if you have any questions.

Thanks,
"""


msg = f'Subject:{subject}\n\n{body}'

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
text = message.as_string()

#message.attach(MIMEText(body, "plain"))
# Open PDF file in binary mode
filename= 'file1.pdf'

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        for name, email,in reader:
            server.sendmail(sender_email,email,body.format(name=name))

# with open(filename, "rb") as attachment:
#     # Add file as application/octet-stream
#     # Email client can usually download this automatically as attachment
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())
#
# # Encode file in ASCII characters to send by email
# encoders.encode_base64(part)
#
# # Add header as key/value pair to attachment part
# part.add_header(
#     "Content-Disposition",
#     f"attachment; filename= {filename}",
# )
#
# # Add attachment to message and convert message to string
# message.attach(part)
# text = message.as_string()

# Log in to server using secure context and send email
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, text)
