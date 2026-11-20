# Previous input
date_or_dt_str = input("Enter date or datetime (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS): ")

# Process
from datetime import datetime

def to_Iso_Format(date_or_dt_str):
    s = date_or_dt_str.strip()
    if " " in s:
        return datetime.strptime(s, "%Y-%m-%d %H:%M:%S").isoformat()
    return datetime.strptime(s, "%Y-%m-%d").date().isoformat()

# Post process
print("ISO 8601 format:", to_Iso_Format(date_or_dt_str))
