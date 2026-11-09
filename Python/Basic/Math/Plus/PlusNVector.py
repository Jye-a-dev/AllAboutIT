# Previous input
a = int(input("Enter the number of vectors to add: "))
# Process
for i in range(a):
    print("Vector", i + 1)
    print(f"Enter the components of the vector {i + 1}:")
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    if i == 0:
        v1 = [n1, n2]
    else:
        v2 = [n1, n2]
        v1 = [v1[0] + v2[0], v1[1] + v2[1]]
# Post process
print("The sum of the vectors is:", v1)
