# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")
days = int(input("Enter number of days to subtract: "))

# Process
from datetime import datetime, timedelta

def subtract_Days_From_Date(date_str, days):
    d = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    res = d - timedelta(days=int(days))
    return res.strftime("%Y-%m-%d")

# Post process
print("Resulting date:", subtract_Days_From_Date(date_str, days))
