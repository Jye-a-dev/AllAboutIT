# Previous input
n1 = input("Enter the base time in day[hh:mm:ss]: ")
n2 = input("Enter the time to add [hh:mm:ss]: ")

# Process
def add_times(time1, time2):
    def to_seconds(time):
        time = time.strip()
        if "[" in time and "]" in time:
            day_part, time_part = time.split("[", 1)
            days = int(day_part.strip())
            time = time_part.rstrip("]")
        else:
            days = 0

        hours, minutes, seconds = map(int, time.split(":"))
        return days * 86400 + hours * 3600 + minutes * 60 + seconds
    total = to_seconds(time1) + to_seconds(time2)
    years, remainder = divmod(total, 365 * 24 * 3600)
    months, remainder = divmod(remainder, 30 * 24 * 3600)
    weeks, remainder = divmod(remainder, 7 * 24 * 3600)
    days, remainder = divmod(remainder, 24 * 3600)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{years} year, {months} month, {weeks} week, {days} day, {hours:02}:{minutes:02}:{seconds:02}"
# Post process
print("The combined time of", n1, "and", n2, "is:", add_times(n1, n2))