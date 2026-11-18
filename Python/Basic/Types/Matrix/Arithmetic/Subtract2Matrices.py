# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("First matrix")
m1 = [[int(input(f"Enter element [{i}][{j}] for m1: ")) for j in range(cols)] for i in range(rows)]
print("Second matrix")
m2 = [[int(input(f"Enter element [{i}][{j}] for m2: ")) for j in range(cols)] for i in range(rows)]

# Process
def subtract_2_Matrices(m1, m2):
    if len(m1) != len(m2) or any(len(r1) != len(r2) for r1, r2 in zip(m1, m2)):
        raise ValueError("Matrices must have identical dimensions")
    return [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

# Post process
try:
    print("Difference of two matrices:", subtract_2_Matrices(m1, m2))
except Exception as e:
    print("Cannot subtract matrices:", e)
