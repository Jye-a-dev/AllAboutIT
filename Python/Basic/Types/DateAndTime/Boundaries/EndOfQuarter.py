# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
import calendar
from datetime import date, datetime

def get_End_Of_Quarter(date_str):
    d = datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").date()
    start_month = ((d.month - 1) // 3) * 3 + 1
    end_month = start_month + 2
    last_day = calendar.monthrange(d.year, end_month)[1]
    return date(d.year, end_month, last_day).strftime("%Y-%m-%d")

# Post process
print("End of quarter:", get_End_Of_Quarter(date_str))
