# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def is_Weekday(date_str):
    dt = datetime.strptime(date_str.strip(), "%Y-%m-%d")
    return dt.weekday() < 5

# Post process
print("Is weekday:", is_Weekday(date_str))
