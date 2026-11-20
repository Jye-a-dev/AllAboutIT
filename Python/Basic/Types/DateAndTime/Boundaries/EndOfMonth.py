# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
import calendar
from datetime import date, datetime

def get_End_Of_Month(date_str):
    d = datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").date()
    last_day = calendar.monthrange(d.year, d.month)[1]
    return date(d.year, d.month, last_day).strftime("%Y-%m-%d")

# Post process
print("End of month:", get_End_Of_Month(date_str))
