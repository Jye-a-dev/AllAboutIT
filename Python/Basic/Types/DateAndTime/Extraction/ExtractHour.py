# Previous input
time_str = input("Enter time (HH:MM:SS): ")

# Process
def get_Hour(time_str):
    part = time_str.strip().split()[-1]
    return int(part.split(":")[0])

# Post process
print("Hour extracted:", get_Hour(time_str))
