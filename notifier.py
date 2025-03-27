import os
import sqlite3
import datetime
import pyttsx3
from plyer import notification
import yagmail
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def speak(message):
    """Convert text to speech"""
    engine.say(message)
    engine.runAndWait()

def send_email(subject, body):
    """Send email notification"""
    try:
        yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
        yag.send(RECIPIENT_EMAIL, subject, body)
        print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def notify_user(title, message):
    """Show system notification, voice alert, and email"""
    notification.notify(title=title, message=message, app_name="Medicine Tracker", timeout=5)
    speak(message)
    send_email(title, message)

def check_medicine_status():
    """Check expiry and refill reminders"""
    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()

    today = datetime.date.today()
    
    cursor.execute("SELECT name, expiry_date, purchase_date, duration FROM medicines")
    medicines = cursor.fetchall()
    conn.close()

    for med in medicines:
        name, expiry_date, purchase_date, duration = med
        expiry_date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
        finish_date = datetime.datetime.strptime(purchase_date, "%Y-%m-%d").date() + datetime.timedelta(days=int(duration))

        days_to_expiry = (expiry_date - today).days
        days_to_finish = (finish_date - today).days

        if days_to_expiry == 2:
            notify_user(f"Medicine '{name}' is expiring soon!", f"Only {days_to_expiry} days left until expiry.")
        
        if days_to_finish == 2:
            notify_user(f"Refill Reminder for '{name}'", f"Only {days_to_finish} days left before it runs out.")

if __name__ == "__main__":
    check_medicine_status()
