# Previous input
n = int(input("Enter integer number: "))

# Process
def Min_Digit(n):
    return min(int(d) for d in str(abs(n)))

# Post process
print("The minimum digit is:", Min_Digit(n))
