import os


class Config:
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    DEBUG = os.getenv("DEBUG") != "false"
    SMTP_PORT = int(os.getenv("SMTP_PORT"))
    SERVER_PORT = int(os.getenv("SERVER_PORT"))
