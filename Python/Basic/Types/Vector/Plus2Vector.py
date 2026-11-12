# Previous input
print("First vector")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("Second vector")
n11 = int(input("Enter first number: "))
n22 = int(input("Enter second number: "))
# Process
def add_vectors(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1]]
# Post process
print("The sum of the two vectors is:", add_vectors([n1, n2], [n11, n22]))
