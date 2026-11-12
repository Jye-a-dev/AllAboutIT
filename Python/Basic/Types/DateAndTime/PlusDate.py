# Previous input
n1 = input("Enter the first date [yy:mm:dd]: ")
n2 = input("Enter the date to add [yy:mm:dd]: ")

# Process
def add_date(date1, date2):
    def to_days(date_value):
        date_value = date_value.strip()
        if "[" in date_value and "]" in date_value:
            day_part, date_part = date_value.split("[", 1)
            extra_days = int(day_part.strip()) if day_part.strip() else 0
            date_value = date_part.rstrip("]")
        else:
            extra_days = 0

        years, months, days = map(int, date_value.split(":"))
        return extra_days + years * 365 + months * 30 + days

    total_days = to_days(date1) + to_days(date2)
    years, remainder = divmod(total_days, 365)
    months, days = divmod(remainder, 30)
    return f"{years} year, {months} month, {days} day"

# Post process
print("The combined date of", n1, "and", n2, "is:", add_date(n1, n2))