# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def get_Day_Of_Week_Name(date_str):
    return datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").strftime("%A")

# Post process
print("Day of week name:", get_Day_Of_Week_Name(date_str))
