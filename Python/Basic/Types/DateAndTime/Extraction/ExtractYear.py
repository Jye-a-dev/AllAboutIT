# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def get_Year(date_str):
    return datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").year

# Post process
print("Year extracted:", get_Year(date_str))
