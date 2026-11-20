# Previous input
start_date_str = input("Enter start date (YYYY-MM-DD): ")
end_date_str = input("Enter end date (YYYY-MM-DD): ")

# Process
from datetime import datetime, timedelta

def generate_Date_Range(start_date_str, end_date_str, step_days=1):
    start = datetime.strptime(start_date_str.strip(), "%Y-%m-%d").date()
    end = datetime.strptime(end_date_str.strip(), "%Y-%m-%d").date()
    step = max(1, int(step_days))
    res = []
    curr = start
    while curr <= end:
        res.append(curr.strftime("%Y-%m-%d"))
        curr += timedelta(days=step)
    return res

# Post process
print("Generated date range:", generate_Date_Range(start_date_str, end_date_str))
