# Previous input
time1_str = input("Enter first time (HH:MM:SS): ")
time2_str = input("Enter second time (HH:MM:SS): ")

# Process
from datetime import datetime

def seconds_Between_Times(time1_str, time2_str):
    t1 = datetime.strptime(time1_str.strip(), "%H:%M:%S")
    t2 = datetime.strptime(time2_str.strip(), "%H:%M:%S")
    return int(abs((t2 - t1).total_seconds()))

# Post process
print("Seconds between times:", seconds_Between_Times(time1_str, time2_str))
