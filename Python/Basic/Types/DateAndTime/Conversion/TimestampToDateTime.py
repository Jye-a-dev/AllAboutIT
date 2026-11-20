# Previous input
ts = float(input("Enter Unix timestamp: "))

# Process
from datetime import datetime

def from_Unix_Timestamp(timestamp):
    return datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d %H:%M:%S")

# Post process
print("Datetime string:", from_Unix_Timestamp(ts))
