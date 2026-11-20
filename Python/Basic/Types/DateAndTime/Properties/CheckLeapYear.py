# Previous input
year = int(input("Enter year: "))

# Process
import calendar

def is_Leap_Year(year):
    return calendar.isleap(int(year))

# Post process
print("Is leap year:", is_Leap_Year(year))
