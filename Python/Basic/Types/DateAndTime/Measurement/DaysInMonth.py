# Previous input
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Process
import calendar

def get_Days_In_Month(year, month):
    return calendar.monthrange(int(year), int(month))[1]

# Post process
print(f"Days in month {month}/{year}:", get_Days_In_Month(year, month))
