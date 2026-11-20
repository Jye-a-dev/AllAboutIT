# Previous input
time_str = input("Enter time in 12-hour format (e.g. 02:30:00 PM): ")

# Process
from datetime import datetime

def to_24_Hour_Format(time_str):
    s = time_str.strip()
    for fmt in ("%I:%M:%S %p", "%I:%M %p"):
        try:
            return datetime.strptime(s, fmt).strftime("%H:%M:%S")
        except ValueError:
            pass
    return datetime.strptime(s, "%H:%M:%S").strftime("%H:%M:%S")

# Post process
print("24-hour format:", to_24_Hour_Format(time_str))
