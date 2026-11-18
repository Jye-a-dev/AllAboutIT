# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("First matrix")
m1 = [[int(input(f"Enter element [{i}][{j}] for m1: ")) for j in range(cols)] for i in range(rows)]
print("Second matrix")
m2 = [[int(input(f"Enter element [{i}][{j}] for m2: ")) for j in range(cols)] for i in range(rows)]

# Process
def is_Equal_Matrices(m1, m2, tolerance=1e-9):
    if len(m1) != len(m2):
        return False
    for r1, r2 in zip(m1, m2):
        if len(r1) != len(r2):
            return False
        for v1, v2 in zip(r1, r2):
            if abs(v1 - v2) > tolerance:
                return False
    return True

# Post process
print("Are matrices equal:", is_Equal_Matrices(m1, m2))
