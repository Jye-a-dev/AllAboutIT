# Previous input
time_str = input("Enter time (HH:MM:SS): ")

# Process
def time_To_Minutes(time_str):
    parts = [int(p) for p in time_str.strip().split(":")]
    return round(parts[0] * 60 + parts[1] + parts[2] / 60.0, 2)

# Post process
print("Total minutes:", time_To_Minutes(time_str))
