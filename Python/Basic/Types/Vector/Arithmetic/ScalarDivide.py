# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]
k = float(input("Enter scalar value: "))

# Process
def scalar_Divide(v, k):
    if k == 0:
        raise ZeroDivisionError("Cannot divide a vector by zero")
    return [x / k for x in v]

# Post process
print("Scalar divided vector:", scalar_Divide(v, k))
