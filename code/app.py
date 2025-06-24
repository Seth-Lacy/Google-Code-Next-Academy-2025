import os
from flask import Flask, request, send_from_directory
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

load_dotenv()

app = Flask(__name__,static_folder='.',static_url_path='')

@app.route('/')
def index():
    return send_from_directory(".", "index.html")

@app.route("/send", methods=["POST"])
def send_email():
    name = request.form["name"]
    sender = request.form["email"]
    message = request.form["message"]

subject = f"Meassage from {name}"
body = f"From: {name} <{sender}>\n\n{message}"
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = os.environ['SMTP_USER']
msg["To"] = sender

with smtplib.SMTP_SSL(
    os.environ['SMTP_HOST'],
    int(os.environ['SMTP_PORT'])
) as server:
    server.login(os.environ["SMTP_USER"], os.environ["SMTP_PASS"])
    server.sendmail(
    os.environ["SMTP_USER"],
    [sender],
    msg.as_string()
    )
return send_from_directory('.', index.html)

if __name__ == '__main__':
    app.run()



