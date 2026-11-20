# Previous input
dt_str = input("Enter datetime (YYYY-MM-DD HH:MM:SS): ")

# Process
from datetime import datetime

def to_Unix_Timestamp(dt_str):
    s = dt_str.strip()
    fmt = "%Y-%m-%d %H:%M:%S" if " " in s else "%Y-%m-%d"
    dt = datetime.strptime(s, fmt)
    return int(dt.timestamp())

# Post process
print("Unix timestamp:", to_Unix_Timestamp(dt_str))
