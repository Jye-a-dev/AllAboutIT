# Previous input
a = int(input("Enter the number of matrices to add: "))
r = int(input("Enter the number of rows in the matrices: "))
c = int(input("Enter the number of columns in the matrices: "))
# Process
def plus_Matries(a, r, c):
    m1 = []
    for i in range(a):
        print("Matrix", i + 1)
        matrix = []
        for j in range(r):
            row = []
            for k in range(c):
                num = int(input(f"Enter number for row {j + 1}, column {k + 1}: "))
                row.append(num)
            matrix.append(row)
        if i == 0:
            m1 = matrix
        else:
            m2 = matrix
            m1 = [[m1[x][y] + m2[x][y] for y in range(c)] for x in range(r)]
    return m1

def add_N_Matrices(matrices):
    if not matrices:
        return []
    res = [[val for val in row] for row in matrices[0]]
    for m in matrices[1:]:
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] += m[i][j]
    return res

plus_matrices = plus_Matries
# Post process
print("The sum of the matrices is:", plus_Matries(a, r, c))
