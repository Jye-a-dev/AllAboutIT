# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def get_Day(date_str):
    return datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").day

# Post process
print("Day extracted:", get_Day(date_str))
