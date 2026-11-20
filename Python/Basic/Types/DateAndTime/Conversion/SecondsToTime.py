# Previous input
seconds = int(input("Enter seconds: "))

# Process
def seconds_To_Time(seconds):
    total = int(seconds) % 86400
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02}:{m:02}:{s:02}"

# Post process
print("Time string (HH:MM:SS):", seconds_To_Time(seconds))
