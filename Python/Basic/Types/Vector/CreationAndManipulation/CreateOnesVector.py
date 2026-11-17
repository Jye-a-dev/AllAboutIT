# Previous input
dim = int(input("Enter vector dimension: "))

# Process
def create_Ones_Vector(dim):
    if dim < 0:
        raise ValueError("Dimension must be non-negative")
    return [1.0] * dim

# Post process
print("Created ones vector:", create_Ones_Vector(dim))
