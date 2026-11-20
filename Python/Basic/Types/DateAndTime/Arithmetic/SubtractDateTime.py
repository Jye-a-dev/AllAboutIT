# Previous input
dt1_str = input("Enter first datetime (YYYY-MM-DD HH:MM:SS): ")
dt2_str = input("Enter second datetime (YYYY-MM-DD HH:MM:SS): ")

# Process
from datetime import datetime

def subtract_DateTime(dt1_str, dt2_str):
    dt1 = datetime.strptime(dt1_str.strip(), "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(dt2_str.strip(), "%Y-%m-%d %H:%M:%S")
    diff = dt1 - dt2
    total_seconds = int(diff.total_seconds())
    sign = "-" if total_seconds < 0 else ""
    total_seconds = abs(total_seconds)
    days, rem = divmod(total_seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{sign}{days} days, {hours:02}:{minutes:02}:{seconds:02}"

# Post process
print("Difference between datetimes:", subtract_DateTime(dt1_str, dt2_str))
