# Previous input
n = int(input("Enter number of matrices: "))
matrices = []
for idx in range(n):
    r = int(input(f"Enter rows of matrix {idx + 1}: "))
    c = int(input(f"Enter cols of matrix {idx + 1}: "))
    mat = [[int(input(f"matrix[{i}][{j}]: ")) for j in range(c)] for i in range(r)]
    matrices.append(mat)

# Process
def multiply_N_Matrices(matrices):
    if not matrices:
        return []
    res = matrices[0]
    for m in matrices[1:]:
        rows1, cols1 = len(res), len(res[0])
        rows2, cols2 = len(m), len(m[0])
        if cols1 != rows2:
            raise ValueError("Incompatible dimensions for matrix multiplication")
        res = [[sum(res[i][k] * m[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    return res

# Post process
try:
    print("Product of N matrices:", multiply_N_Matrices(matrices))
except Exception as e:
    print("Cannot multiply N matrices:", e)
