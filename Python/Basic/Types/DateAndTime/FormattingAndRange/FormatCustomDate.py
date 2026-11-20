# Previous input
date_str = input("Enter date (YYYY-MM-DD): ")
target_format = input("Enter target format (default: %d/%m/%Y): ") or "%d/%m/%Y"

# Process
from datetime import datetime

def format_Custom_Date(date_str, from_format="%Y-%m-%d", to_format="%d/%m/%Y"):
    dt = datetime.strptime(date_str.strip(), from_format)
    return dt.strftime(to_format)

# Post process
print("Formatted date:", format_Custom_Date(date_str, to_format=target_format))
