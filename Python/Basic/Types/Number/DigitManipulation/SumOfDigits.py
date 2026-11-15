# Previous input
n = int(input("Enter integer number: "))

# Process
def sum_Of_Digits(n):
    return sum(int(d) for d in str(abs(n)))

# Post process
print("The sum of digits is:", sum_Of_Digits(n))
