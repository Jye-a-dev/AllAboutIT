# Previous input
date_list = [d.strip() for d in input("Enter dates (comma-separated YYYY-MM-DD): ").split(",") if d.strip()]

# Process
from datetime import datetime

def find_Latest_Date(date_list):
    if not date_list:
        return None
    return max(date_list, key=lambda d: datetime.strptime(d.strip(), "%Y-%m-%d"))

# Post process
print("Latest date in list:", find_Latest_Date(date_list))
