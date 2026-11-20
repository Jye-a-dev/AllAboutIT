# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import date, datetime

def is_Today(date_str):
    dt = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    return dt == date.today()

# Post process
print("Is today:", is_Today(date_str))
