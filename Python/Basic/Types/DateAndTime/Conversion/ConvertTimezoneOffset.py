# Previous input
dt_str = input("Enter datetime (YYYY-MM-DD HH:MM:SS): ")
from_offset = float(input("Enter source UTC offset in hours (e.g. 0 or 7): "))
to_offset = float(input("Enter target UTC offset in hours (e.g. -5 or 9): "))

# Process
from datetime import datetime, timedelta

def convert_Timezone_Offset(dt_str, from_offset_hours, to_offset_hours):
    dt = datetime.strptime(dt_str.strip(), "%Y-%m-%d %H:%M:%S")
    diff_hours = float(to_offset_hours) - float(from_offset_hours)
    target_dt = dt + timedelta(hours=diff_hours)
    return target_dt.strftime("%Y-%m-%d %H:%M:%S")

# Post process
print("Converted datetime:", convert_Timezone_Offset(dt_str, from_offset, to_offset))
