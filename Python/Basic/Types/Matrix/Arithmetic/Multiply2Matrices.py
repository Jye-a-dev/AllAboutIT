# Previous input
r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter cols of first matrix: "))
print("First matrix:")
m1 = [[int(input(f"m1[{i}][{j}]: ")) for j in range(c1)] for i in range(r1)]
c2 = int(input("Enter cols of second matrix: "))
print("Second matrix:")
m2 = [[int(input(f"m2[{i}][{j}]: ")) for j in range(c2)] for i in range(c1)]

# Process
def multiply_2_Matrices(m1, m2):
    if not m1 or not m2:
        return []
    rows1, cols1 = len(m1), len(m1[0])
    rows2, cols2 = len(m2), len(m2[0])
    if cols1 != rows2:
        raise ValueError("Columns of first matrix must equal rows of second matrix")
    return [[sum(m1[i][k] * m2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]

# Post process
try:
    print("Product of two matrices:", multiply_2_Matrices(m1, m2))
except Exception as e:
    print("Cannot multiply matrices:", e)
