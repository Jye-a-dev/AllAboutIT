# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def get_Day_Of_Week_Index(date_str):
    return datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").weekday()

# Post process
print("Day of week index (0=Monday, 6=Sunday):", get_Day_Of_Week_Index(date_str))
