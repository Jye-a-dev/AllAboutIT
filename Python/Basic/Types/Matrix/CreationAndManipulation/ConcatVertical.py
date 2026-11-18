# Previous input
cols = int(input("Enter number of columns: "))
r1 = int(input("Enter number of rows for m1: "))
print("First matrix:")
m1 = [[int(input(f"m1[{i}][{j}]: ")) for j in range(cols)] for i in range(r1)]
r2 = int(input("Enter number of rows for m2: "))
print("Second matrix:")
m2 = [[int(input(f"m2[{i}][{j}]: ")) for j in range(cols)] for i in range(r2)]

# Process
def concat_Vertical(m1, m2):
    if not m1:
        return [list(r) for r in m2]
    if not m2:
        return [list(r) for r in m1]
    if len(m1[0]) != len(m2[0]):
        raise ValueError("Matrices must have the same number of columns for vertical concatenation")
    return [list(r) for r in m1] + [list(r) for r in m2]

# Post process
try:
    print("Vertically concatenated matrix:", concat_Vertical(m1, m2))
except Exception as e:
    print("Cannot concatenate vertically:", e)
