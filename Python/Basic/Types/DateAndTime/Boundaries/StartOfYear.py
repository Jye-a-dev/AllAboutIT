# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import date, datetime

def get_Start_Of_Year(date_str):
    d = datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").date()
    return date(d.year, 1, 1).strftime("%Y-%m-%d")

# Post process
print("Start of year:", get_Start_Of_Year(date_str))
