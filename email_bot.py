import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

# Enter user information
sender_email = 'knowledgef97@gmail.com'
# receiver_email = 'ojalmaps@gmail.com'
password = input('Enter the password:')

subject = "Subject: GraceHacks UCSC Female and Non-Binary Hackathon Sponsorship"

body ="""
<html>
<body style ="font-size:14px;font-family: "Times New Roman"">
<p>
Hi ! <br>
I help organize GraceHacks, an annual, beginner-friendly student-led hackathon for women and non-binary students in tech taking place at the University of California Santa Cruz. We hope to have 100+ women and non-binary students learn new skills in a supportive, low-pressure environment.
<br><br>
<b>  What is GraceHacks? </b><br>
<ul>
<li>GraceHacks is a 12-hour hackathon at the University of California Santa Cruz for female and non-binary students and includes a day full of hacking, learning and using new technologies. </li>
<li>The aim of GraceHacks is to foster a welcoming and supportive hackathon environment for womxn and non-binary students. GraceHacks strives to empower these underrepresented groups and ensure that they have the confidence to create without inherent bias or sexism and to encourage their passion to excel in STEM fields.</li>
<li>GraceHacks successfully held its first virtual hackathon in October 2020 with over 100 women/non-binary attendees.</li>
</ul><br>
<b>  What we’re looking for: </b><br>
We’re currently looking for <b>sponsors</b> to make this year’s hackathon possible. We hope to hold this year’s hackathon during November at the University of California Santa Cruz. If COVID-19 situations do not allow an in-person event, we will be holding our event virtually.
<br><br>
I'm wondering if you think  company_name would be interested in sponsoring. It would be great to have company_name at GraceHacks and would encourage women and non-binary college students to pursue STEM careers.<br>
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
# message["To"] = receiver_email
message["Subject"] = subject
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            receiver_email = row[2]
            message.attach(MIMEText(body.replace("company_name",name), "html"))
            filename = 'GHSponsership-packet.pdf'
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()
            server.sendmail(sender_email, "ojalmaps@gmail.com", text)
            server.sendmail(sender_email, receiver_email, text)

# trying to find a way to send the text as a bold

