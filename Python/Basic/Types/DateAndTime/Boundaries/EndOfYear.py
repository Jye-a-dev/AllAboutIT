# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import date, datetime

def get_End_Of_Year(date_str):
    d = datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").date()
    return date(d.year, 12, 31).strftime("%Y-%m-%d")

# Post process
print("End of year:", get_End_Of_Year(date_str))
