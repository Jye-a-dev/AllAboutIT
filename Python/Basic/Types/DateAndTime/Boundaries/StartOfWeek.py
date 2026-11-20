# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime, timedelta

def get_Start_Of_Week(date_str):
    d = datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").date()
    monday = d - timedelta(days=d.weekday())
    return monday.strftime("%Y-%m-%d")

# Post process
print("Start of week (Monday):", get_Start_Of_Week(date_str))
