# Previous input
a = int(input("Enter the number of numbers to subtract: "))
# Process
def minus_numbers(a):
    total = 0
    for i in range(a):
        n = int(input("Enter a number: "))
        total -= n
    return total
# Post process
print("The difference of the entered numbers is:", minus_numbers(a))