# Previous input
time_str = input("Enter time (HH:MM:SS): ")

# Process
from datetime import datetime

def is_Valid_Time(time_str):
    try:
        datetime.strptime(time_str.strip(), "%H:%M:%S")
        return True
    except (ValueError, AttributeError):
        return False

# Post process
print("Is valid time:", is_Valid_Time(time_str))
