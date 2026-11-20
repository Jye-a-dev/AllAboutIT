# Previous input
dt_str = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")

# Process
from datetime import datetime

def is_Valid_DateTime(dt_str):
    try:
        datetime.strptime(dt_str.strip(), "%Y-%m-%d %H:%M:%S")
        return True
    except (ValueError, AttributeError):
        return False

# Post process
print("Is valid datetime:", is_Valid_DateTime(dt_str))
