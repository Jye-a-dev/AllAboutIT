# Previous input
dim = int(input("Enter vector dimension: "))
index = int(input("Enter basis index (0-based): "))

# Process
def create_Basis_Vector(dim, index):
    if dim <= 0:
        raise ValueError("Dimension must be positive")
    if not (0 <= index < dim):
        raise IndexError("Basis index out of range")
    res = [0.0] * dim
    res[index] = 1.0
    return res

# Post process
print("Created standard basis vector:", create_Basis_Vector(dim, index))
