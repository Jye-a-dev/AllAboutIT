# Previous input
month_input = input("Enter month number (1-12) or date (YYYY-MM-DD): ")

# Process
import calendar
from datetime import datetime

def get_Month_Name(month_or_date):
    val = str(month_or_date).strip()
    if val.isdigit():
        m = int(val)
    else:
        m = datetime.strptime(val.split()[0], "%Y-%m-%d").month
    return calendar.month_name[m]

# Post process
print("Month name:", get_Month_Name(month_input))
