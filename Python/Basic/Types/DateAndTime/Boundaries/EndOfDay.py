# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def get_End_Of_Day(date_str):
    d = datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").date()
    return f"{d.strftime('%Y-%m-%d')} 23:59:59"

# Post process
print("End of day:", get_End_Of_Day(date_str))
