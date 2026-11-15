# Previous input
n = int(input("Enter integer number: "))

# Process
def split_Digits(n):
    return [int(d) for d in str(abs(n))]

# Post process
print("The digits of the number are:", split_Digits(n))
