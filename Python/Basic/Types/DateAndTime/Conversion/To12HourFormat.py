# Previous input
time_str = input("Enter time (HH:MM:SS): ")

# Process
from datetime import datetime

def to_12_Hour_Format(time_str):
    t = datetime.strptime(time_str.strip(), "%H:%M:%S")
    return t.strftime("%I:%M:%S %p")

# Post process
print("12-hour format:", to_12_Hour_Format(time_str))
