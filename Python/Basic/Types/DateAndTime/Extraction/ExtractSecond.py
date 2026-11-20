# Previous input
time_str = input("Enter time (HH:MM:SS): ")

# Process
def get_Second(time_str):
    part = time_str.strip().split()[-1]
    return int(part.split(":")[2])

# Post process
print("Second extracted:", get_Second(time_str))
