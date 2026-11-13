# Previous input
a = int(input("Enter the number of numbers to divide: "))
# Process
def divide_numbers(a):
    total = 1
    for i in range(a):
        n = int(input("Enter a number: "))
        total /= n
    return total
# Post process
print("The quotient of the entered numbers is:", divide_numbers(a))