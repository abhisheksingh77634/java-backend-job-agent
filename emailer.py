import os

import smtplib

from email.mime.text import MIMEText

def send_email(job_list):

    sender = os.getenv("EMAIL_USER")

    password = os.getenv("EMAIL_PASS")

    receiver = os.getenv("TO_EMAIL")

    body = "Java Backend Visa-Sponsored Jobs (Daily)\n\n"

    for job in job_list:

        body += f"""

{job['country']}

• {job['title'].title()}

  Match: {job['score']}%

  Apply: {job['link']}

"""

    msg = MIMEText(body)

    msg["Subject"] = "Daily Java Backend Visa Jobs"

    msg["From"] = sender

    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

        server.login(sender, password)

        server.send_message(msg)
 
