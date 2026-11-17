# Previous input
v1 = [float(x) for x in input("Enter first vector (comma-separated): ").split(",")]
v2 = [float(x) for x in input("Enter second vector (comma-separated): ").split(",")]
p = float(input("Enter order p (>= 1): "))

# Process
def minkowski_Distance(v1, v2, p=3):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    if p < 1:
        raise ValueError("p must be greater than or equal to 1")
    return sum(abs(a - b)**p for a, b in zip(v1, v2))**(1 / p)

# Post process
print("Minkowski distance:", minkowski_Distance(v1, v2, p))
