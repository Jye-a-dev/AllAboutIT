# Previous input
import math
num = float(input("Enter number: "))

# Process
def truncate_Number(n):
    return math.trunc(n)

# Post process
print("The truncated number is:", truncate_Number(num))
