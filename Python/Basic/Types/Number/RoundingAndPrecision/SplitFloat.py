# Previous input
import math
num = float(input("Enter float number: "))

# Process
def split_Float(n):
    frac_part, int_part = math.modf(n)
    return int(int_part), frac_part

# Post process
print("The integer and fractional parts are:", split_Float(num))
