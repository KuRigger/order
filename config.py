import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
APPLICATIONS_FILE = "applications.json"
APPROVED_FILE = "approved.json"
GIFT_PDF_PATH = "static\подарок.pdf"