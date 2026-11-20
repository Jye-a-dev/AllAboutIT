# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def get_Quarter_Of_Year(date_str):
    m = datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").month
    return (m - 1) // 3 + 1

# Post process
print("Quarter of year (1-4):", get_Quarter_Of_Year(date_str))
