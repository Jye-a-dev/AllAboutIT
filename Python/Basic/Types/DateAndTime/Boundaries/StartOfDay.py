# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def get_Start_Of_Day(date_str):
    d = datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").date()
    return f"{d.strftime('%Y-%m-%d')} 00:00:00"

# Post process
print("Start of day:", get_Start_Of_Day(date_str))
