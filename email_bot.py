import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

# Enter user information
while(True):
    sender_email = input('Enter your email :')
    if "@" in sender_email:
        break


password = input('Enter the password :')

#From the Google Document
subject = "Subject: GraceHacks UCSC Female and Non-Binary Hackathon Sponsorship"
body ="""
<html>
<body style ="font-size:14px;font-family: "Times New Roman"">
<p>
Hi ! <br>
Summary about hacakthon venue 
<br><br>
<b>  What is xHacks? </b><br>
<ul>
<li> Item 1 </li>
<li>  Item 2 </li>
</ul><br>
<b>  What we’re looking for: </b><br>
??
<br><br>
I'm wondering if you think  company_name would be interested in sponsoring. It would be great to have company_name at x Hacks.<br>
I have attached the sponsorship packet to this email.<br>
Please let me know if you have any questions.<br>
<br> <br>
Thanks.
</p>
</body>
</html>
"""

message = MIMEMultipart()
message["From"] = sender_email

context = ssl.create_default_context()
company_names =[]

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
except Exception as e:
    print(e)
    exit(-1)

with open("contacts.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        name = row[0]
        company_names.append(name)
        receiver_email = row[2]
        message["To"] = receiver_email
        message["Subject"] = subject
        text = message.as_string()
        message.attach(MIMEText(body.replace("company_name",name), "html"))
        filename = 'Sponsership-packet.pdf'                                    # Name of the file.
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        message.attach(part)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)



print('The emails have been sent to the following companies!')
print(company_names)
