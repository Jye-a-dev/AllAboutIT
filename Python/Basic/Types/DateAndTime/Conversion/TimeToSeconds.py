# Previous input
time_str = input("Enter time (HH:MM:SS): ")

# Process
def time_To_Seconds(time_str):
    parts = [int(p) for p in time_str.strip().split(":")]
    return parts[0] * 3600 + parts[1] * 60 + parts[2]

# Post process
print("Total seconds:", time_To_Seconds(time_str))
