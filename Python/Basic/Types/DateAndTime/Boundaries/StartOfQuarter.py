# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import date, datetime

def get_Start_Of_Quarter(date_str):
    d = datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").date()
    start_month = ((d.month - 1) // 3) * 3 + 1
    return date(d.year, start_month, 1).strftime("%Y-%m-%d")

# Post process
print("Start of quarter:", get_Start_Of_Quarter(date_str))
