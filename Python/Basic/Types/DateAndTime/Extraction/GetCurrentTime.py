# Previous input
# No user input required for current time

# Process
from datetime import datetime

def get_Current_Time():
    return datetime.now().strftime("%H:%M:%S")

# Post process
print("Current time:", get_Current_Time())
