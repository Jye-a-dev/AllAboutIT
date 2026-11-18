# Previous input
rows = int(input("Enter number of rows: "))
c1 = int(input("Enter number of columns for m1: "))
print("First matrix:")
m1 = [[int(input(f"m1[{i}][{j}]: ")) for j in range(c1)] for i in range(rows)]
c2 = int(input("Enter number of columns for m2: "))
print("Second matrix:")
m2 = [[int(input(f"m2[{i}][{j}]: ")) for j in range(c2)] for i in range(rows)]

# Process
def concat_Horizontal(m1, m2):
    if len(m1) != len(m2):
        raise ValueError("Matrices must have the same number of rows for horizontal concatenation")
    return [list(r1) + list(r2) for r1, r2 in zip(m1, m2)]

# Post process
try:
    print("Horizontally concatenated matrix:", concat_Horizontal(m1, m2))
except Exception as e:
    print("Cannot concatenate horizontally:", e)
