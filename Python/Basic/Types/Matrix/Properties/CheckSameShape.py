# Previous input
rows1 = int(input("Enter number of rows for m1: "))
cols1 = int(input("Enter number of columns for m1: "))
m1 = [[int(input(f"m1[{i}][{j}]: ")) for j in range(cols1)] for i in range(rows1)]

rows2 = int(input("Enter number of rows for m2: "))
cols2 = int(input("Enter number of columns for m2: "))
m2 = [[int(input(f"m2[{i}][{j}]: ")) for j in range(cols2)] for i in range(rows2)]

# Process
def is_Same_Shape(m1, m2):
    if len(m1) != len(m2):
        return False
    return all(len(r1) == len(r2) for r1, r2 in zip(m1, m2))

# Post process
print("Matrices have same shape:", is_Same_Shape(m1, m2))
