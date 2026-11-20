# Previous input
date1_str = input("Enter first date (YYYY-MM-DD): ")
date2_str = input("Enter second date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def is_Same_Day(date1_str, date2_str):
    d1 = datetime.strptime(date1_str.strip(), "%Y-%m-%d").date()
    d2 = datetime.strptime(date2_str.strip(), "%Y-%m-%d").date()
    return d1 == d2

# Post process
print("Are dates the same day:", is_Same_Day(date1_str, date2_str))
