# Previous input
a = int(input("Enter the number of numbers to multiply: "))
# Process
def multiply_numbers(a):
    total = 1
    for i in range(a):
        n = int(input("Enter a number: "))
        total *= n
    return total
# Post process
print("The product of the entered numbers is:", multiply_numbers(a))