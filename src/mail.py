import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from config import Config
from io import BytesIO


class Email:
    def __init__(self, receiver: str, subject: str, doc: BytesIO):
        self.receiver = receiver
        self.subject = subject
        self.doc = doc

    def send(self):
        msg = MIMEMultipart()
        msg["From"] = Config.EMAIL_HOST_USER
        msg["To"] = self.receiver
        msg["Subject"] = self.subject

        part = MIMEBase("application", "octet-stream")
        part.set_payload(self.doc.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition", f"attachment; filename={self.subject}.docx"
        )
        msg.attach(part)

        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
            server.starttls()
            server.login(Config.EMAIL_HOST_USER, Config.EMAIL_HOST_PASSWORD)
            server.sendmail(Config.EMAIL_HOST_USER, self.receiver, msg.as_string())
