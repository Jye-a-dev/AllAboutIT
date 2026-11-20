# Previous input
birth_date_str = input("Enter birth date (YYYY-MM-DD): ")

# Process
from datetime import date, datetime

def calculate_Age(birth_date_str, reference_date_str=None):
    birth_date = datetime.strptime(birth_date_str.strip(), "%Y-%m-%d").date()
    if reference_date_str:
        ref_date = datetime.strptime(reference_date_str.strip(), "%Y-%m-%d").date()
    else:
        ref_date = date.today()
    age = ref_date.year - birth_date.year
    if (ref_date.month, ref_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return max(0, age)

# Post process
print("Calculated age:", calculate_Age(birth_date_str))
