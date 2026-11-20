# Previous input
date_str = input("Enter date to check (YYYY-MM-DD): ")
start_date_str = input("Enter start date (YYYY-MM-DD): ")
end_date_str = input("Enter end date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def is_Date_In_Range(date_str, start_date_str, end_date_str):
    d = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    start = datetime.strptime(start_date_str.strip(), "%Y-%m-%d").date()
    end = datetime.strptime(end_date_str.strip(), "%Y-%m-%d").date()
    if start > end:
        start, end = end, start
    return start <= d <= end

# Post process
print("Is date in range:", is_Date_In_Range(date_str, start_date_str, end_date_str))
