# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime, timedelta

def get_Previous_Business_Day(date_str):
    d = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    curr = d - timedelta(days=1)
    while curr.weekday() >= 5:
        curr -= timedelta(days=1)
    return curr.strftime("%Y-%m-%d")

# Post process
print("Previous business day:", get_Previous_Business_Day(date_str))
