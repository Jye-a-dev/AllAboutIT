# Previous input
iso_str = input("Enter ISO string: ")

# Process
from datetime import datetime

def from_Iso_Format(iso_str):
    dt = datetime.fromisoformat(iso_str.strip())
    if dt.time() != datetime.min.time():
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    return dt.strftime("%Y-%m-%d")

# Post process
print("Standard date/datetime format:", from_Iso_Format(iso_str))
