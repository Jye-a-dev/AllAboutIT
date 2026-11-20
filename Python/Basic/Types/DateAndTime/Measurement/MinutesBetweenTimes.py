# Previous input
time1_str = input("Enter first time (HH:MM:SS): ")
time2_str = input("Enter second time (HH:MM:SS): ")

# Process
from datetime import datetime

def minutes_Between_Times(time1_str, time2_str):
    t1 = datetime.strptime(time1_str.strip(), "%H:%M:%S")
    t2 = datetime.strptime(time2_str.strip(), "%H:%M:%S")
    secs = abs((t2 - t1).total_seconds())
    return round(secs / 60.0, 2)

# Post process
print("Minutes between times:", minutes_Between_Times(time1_str, time2_str))
