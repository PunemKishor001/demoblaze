import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.demoblaze.com"
)

HEADLESS = os.getenv(
    "HEADLESS",
    "true"
).lower() == "true"

USERNAME = os.getenv("DEMOBLAZE_USERNAME")
PASSWORD = os.getenv("DEMOBLAZE_PASSWORD")