# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")
years = int(input("Enter number of years to subtract: "))

# Process
import calendar
from datetime import date, datetime

def subtract_Years_From_Date(date_str, years):
    d = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    new_year = d.year - int(years)
    max_day = calendar.monthrange(new_year, d.month)[1]
    new_day = min(d.day, max_day)
    return date(new_year, d.month, new_day).strftime("%Y-%m-%d")

# Post process
print("Resulting date:", subtract_Years_From_Date(date_str, years))
