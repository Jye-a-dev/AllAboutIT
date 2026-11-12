# Previous input
n1 = (input("Enter the base time [hh:mm:ss]: "))
n2 = (input("Enter the time to add [hh:mm:ss]: "))
# Process
def add_times(time1, time2):
    def to_seconds(time):
        hours, minutes, seconds = map(int, time.split(":"))
        return hours * 3600 + minutes * 60 + seconds

    total = to_seconds(time1) + to_seconds(time2)
    hours, remainder = divmod(total, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02}:{minutes:02}:{seconds:02}"
# Post process
print("The combined time of", n1, "and", n2, "is:", add_times(n1, n2))