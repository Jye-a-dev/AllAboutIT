# Previous input
print("First vector")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("Second vector")
n11 = int(input("Enter first number: "))
n22 = int(input("Enter second number: "))

# Process
def subtract_2_Vectors(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    return [v1[0] - v2[0], v1[1] - v2[1]]

# Post process
print("The difference of the two vectors is:", subtract_2_Vectors([n1, n2], [n11, n22]))
