# Previous input
dt1_str = input("Enter first datetime (YYYY-MM-DD HH:MM:SS): ")
dt2_str = input("Enter second datetime (YYYY-MM-DD HH:MM:SS): ")

# Process
from datetime import datetime

def hours_Between_DateTimes(dt1_str, dt2_str):
    dt1 = datetime.strptime(dt1_str.strip(), "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(dt2_str.strip(), "%Y-%m-%d %H:%M:%S")
    return round(abs((dt2 - dt1).total_seconds()) / 3600.0, 2)

# Post process
print("Hours between datetimes:", hours_Between_DateTimes(dt1_str, dt2_str))
