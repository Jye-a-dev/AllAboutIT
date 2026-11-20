# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")
weeks = int(input("Enter number of weeks to subtract: "))

# Process
from datetime import datetime, timedelta

def subtract_Weeks_From_Date(date_str, weeks):
    d = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    res = d - timedelta(weeks=int(weeks))
    return res.strftime("%Y-%m-%d")

# Post process
print("Resulting date:", subtract_Weeks_From_Date(date_str, weeks))
