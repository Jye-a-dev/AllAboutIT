# Previous input
date_list = [d.strip() for d in input("Enter dates (comma-separated YYYY-MM-DD): ").split(",") if d.strip()]

# Process
from datetime import datetime

def sort_Dates_Ascending(date_list, reverse=False):
    return sorted(date_list, key=lambda d: datetime.strptime(d.strip(), "%Y-%m-%d"), reverse=reverse)

# Post process
print("Sorted dates:", sort_Dates_Ascending(date_list))
