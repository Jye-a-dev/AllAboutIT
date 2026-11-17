# Previous input
dim = int(input("Enter vector dimension: "))

# Process
def create_Zero_Vector(dim):
    if dim < 0:
        raise ValueError("Dimension must be non-negative")
    return [0.0] * dim

# Post process
print("Created zero vector:", create_Zero_Vector(dim))
