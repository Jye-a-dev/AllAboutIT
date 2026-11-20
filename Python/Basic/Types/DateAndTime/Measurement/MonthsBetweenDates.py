# Previous input
date1_str = input("Enter first date (YYYY-MM-DD): ")
date2_str = input("Enter second date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def months_Between_Dates(date1_str, date2_str):
    d1 = datetime.strptime(date1_str.strip(), "%Y-%m-%d").date()
    d2 = datetime.strptime(date2_str.strip(), "%Y-%m-%d").date()
    if d1 > d2:
        d1, d2 = d2, d1
    months = (d2.year - d1.year) * 12 + (d2.month - d1.month)
    if d2.day < d1.day:
        months -= 1
    return max(0, months)

# Post process
print("Full months between dates:", months_Between_Dates(date1_str, date2_str))
