# Previous input
a = int(input("Enter the number of numbers to add: "))

# Process
def add_N_Numbers(a):
    total = 0
    for i in range(a):
        n = int(input("Enter a number: "))
        total += n
    return total

# Post process
print("The sum of the entered numbers is:", add_N_Numbers(a))
