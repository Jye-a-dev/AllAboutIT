# Previous input
date1_str = input("Enter first date (YYYY-MM-DD): ")
date2_str = input("Enter second date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def weeks_Between_Dates(date1_str, date2_str):
    d1 = datetime.strptime(date1_str.strip(), "%Y-%m-%d").date()
    d2 = datetime.strptime(date2_str.strip(), "%Y-%m-%d").date()
    return abs((d2 - d1).days) // 7

# Post process
print("Full weeks between dates:", weeks_Between_Dates(date1_str, date2_str))
