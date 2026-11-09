# Previous input
a = int(input("Enter the number of numbers to add: "))
# Process
total = 0
for i in range(a):
    n = int(input("Enter a number: "))
    total += n
# Post process
print("The sum of the entered numbers is:", total)