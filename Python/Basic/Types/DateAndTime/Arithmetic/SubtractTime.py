# Previous input
time1_str = input("Enter base time (HH:MM:SS): ")
time2_str = input("Enter time to subtract (HH:MM:SS): ")

# Process
from datetime import datetime

def subtract_Time(time1_str, time2_str):
    t1 = datetime.strptime(time1_str.strip(), "%H:%M:%S")
    t2 = datetime.strptime(time2_str.strip(), "%H:%M:%S")
    s1 = t1.hour * 3600 + t1.minute * 60 + t1.second
    s2 = t2.hour * 3600 + t2.minute * 60 + t2.second
    diff = (s1 - s2) % 86400
    h, rem = divmod(diff, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02}:{m:02}:{s:02}"

# Post process
print("Resulting time:", subtract_Time(time1_str, time2_str))
