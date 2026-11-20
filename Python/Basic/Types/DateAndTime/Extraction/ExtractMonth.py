# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def get_Month(date_str):
    return datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").month

# Post process
print("Month extracted:", get_Month(date_str))
