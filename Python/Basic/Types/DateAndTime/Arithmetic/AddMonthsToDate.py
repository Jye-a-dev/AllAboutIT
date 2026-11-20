# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")
months = int(input("Enter number of months to add: "))

# Process
import calendar
from datetime import date, datetime

def add_Months_To_Date(date_str, months):
    d = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    total_months = d.year * 12 + (d.month - 1) + int(months)
    new_year = total_months // 12
    new_month = (total_months % 12) + 1
    max_day = calendar.monthrange(new_year, new_month)[1]
    new_day = min(d.day, max_day)
    return date(new_year, new_month, new_day).strftime("%Y-%m-%d")

# Post process
print("Resulting date:", add_Months_To_Date(date_str, months))
