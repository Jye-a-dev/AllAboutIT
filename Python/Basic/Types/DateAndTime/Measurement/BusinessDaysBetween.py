# Previous input
date1_str = input("Enter first date (YYYY-MM-DD): ")
date2_str = input("Enter second date (YYYY-MM-DD): ")

# Process
from datetime import datetime, timedelta

def count_Business_Days(date1_str, date2_str):
    d1 = datetime.strptime(date1_str.strip(), "%Y-%m-%d").date()
    d2 = datetime.strptime(date2_str.strip(), "%Y-%m-%d").date()
    if d1 > d2:
        d1, d2 = d2, d1
    days = 0
    curr = d1
    while curr <= d2:
        if curr.weekday() < 5:
            days += 1
        curr += timedelta(days=1)
    return days

# Post process
print("Business days between dates:", count_Business_Days(date1_str, date2_str))
