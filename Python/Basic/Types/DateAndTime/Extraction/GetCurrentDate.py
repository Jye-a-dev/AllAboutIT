# Previous input
# No user input required for current date

# Process
from datetime import date

def get_Current_Date():
    return date.today().strftime("%Y-%m-%d")

# Post process
print("Current date:", get_Current_Date())
