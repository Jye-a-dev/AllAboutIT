# Previous input
n = int(input("Enter matrix dimension n: "))

# Process
def create_Identity_Matrix(n):
    if n < 0:
        raise ValueError("Dimension must be non-negative")
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Post process
try:
    print("Identity matrix:", create_Identity_Matrix(n))
except Exception as e:
    print("Cannot create identity matrix:", e)
