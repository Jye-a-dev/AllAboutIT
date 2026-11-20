# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import date, datetime

def days_Until_End_Of_Year(date_str):
    d = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    end_of_year = date(d.year, 12, 31)
    return (end_of_year - d).days

# Post process
print("Days until end of the year:", days_Until_End_Of_Year(date_str))
