# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime, timedelta

def get_End_Of_Week(date_str):
    d = datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").date()
    sunday = d + timedelta(days=6 - d.weekday())
    return sunday.strftime("%Y-%m-%d")

# Post process
print("End of week (Sunday):", get_End_Of_Week(date_str))
