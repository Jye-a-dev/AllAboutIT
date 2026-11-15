# Previous input
a = int(input("Enter the number of numbers to subtract: "))

# Process
def subtract_N_Numbers(a):
    total = 0
    for i in range(a):
        n = int(input("Enter a number: "))
        total -= n
    return total

# Post process
print("The difference of the entered numbers is:", subtract_N_Numbers(a))
