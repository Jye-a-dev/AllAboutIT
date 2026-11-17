# Previous input
v1 = [float(x) for x in input("Enter first vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second vector (comma-separated): ").split(",")]

# Process
def hadamard_Divide(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    for b in v2:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by element with zero value")
    return [a / b for a, b in zip(v1, v2)]

# Post process
print("Hadamard division:", hadamard_Divide(v1, v2))
