# Previous input
time_str = input("Enter time (HH:MM:SS): ")

# Process
def get_Minute(time_str):
    part = time_str.strip().split()[-1]
    return int(part.split(":")[1])

# Post process
print("Minute extracted:", get_Minute(time_str))
