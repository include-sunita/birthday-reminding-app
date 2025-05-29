import json
from datetime import datetime
from plyer import notification

# Load birthday data from JSON file
with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

# Get today's date
today = datetime.now().strftime("%m-%d")

# Check for birthdays today
for name, birthdate in birthdays.items():
    if today == datetime.strptime(birthdate, "%Y-%m-%d").strftime("%m-%d"):
        notification.notify(
            title="🎉 Birthday Reminder",
            message=f"Today is {name}'s birthday! 🎂",
            timeout=10  # seconds
        )
