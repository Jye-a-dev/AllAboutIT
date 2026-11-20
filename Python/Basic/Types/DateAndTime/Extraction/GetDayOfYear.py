# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")

# Process
from datetime import datetime

def get_Day_Of_Year(date_str):
    return datetime.strptime(date_str.strip().split()[0], "%Y-%m-%d").timetuple().tm_yday

# Post process
print("Day of year (1-366):", get_Day_Of_Year(date_str))
