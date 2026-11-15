# Previous input
n = int(input("Enter integer number: "))

# Process
def Product_Of_Digits(n):
    prod = 1
    for d in str(abs(n)):
        prod *= int(d)
    return prod

# Post process
print("The product of digits is:", Product_Of_Digits(n))
