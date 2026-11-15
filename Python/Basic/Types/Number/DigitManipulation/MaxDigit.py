# Previous input
n = int(input("Enter integer number: "))

# Process
def Max_Digit(n):
    return max(int(d) for d in str(abs(n)))

# Post process
print("The maximum digit is:", Max_Digit(n))
