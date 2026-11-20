# Previous input
year = int(input("Enter year: "))

# Process
import calendar

def get_Days_In_Year(year):
    return 366 if calendar.isleap(int(year)) else 365

# Post process
print(f"Days in year {year}:", get_Days_In_Year(year))
