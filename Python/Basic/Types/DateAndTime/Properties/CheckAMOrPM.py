# Previous input
time_str = input("Enter time (HH:MM:SS): ")

# Process
from datetime import datetime

def is_AM_Time(time_str):
    t = datetime.strptime(time_str.strip(), "%H:%M:%S").time()
    return t.hour < 12

# Post process
print("Is AM time:", is_AM_Time(time_str))
