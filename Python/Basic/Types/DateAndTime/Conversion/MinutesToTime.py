# Previous input
minutes = float(input("Enter minutes: "))

# Process
def minutes_To_Time(minutes):
    total_secs = int(round(float(minutes) * 60)) % 86400
    h, rem = divmod(total_secs, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02}:{m:02}:{s:02}"

# Post process
print("Time string (HH:MM:SS):", minutes_To_Time(minutes))
