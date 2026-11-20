# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def get_Week_Of_Year(date_str):
    return datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").isocalendar()[1]

# Post process
print("ISO week of year (1-53):", get_Week_Of_Year(date_str))
