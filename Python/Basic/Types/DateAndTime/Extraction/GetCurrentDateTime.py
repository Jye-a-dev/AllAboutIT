# Previous input
# No user input required for current datetime

# Process
from datetime import datetime

def get_Current_DateTime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Post process
print("Current date and time:", get_Current_DateTime())
