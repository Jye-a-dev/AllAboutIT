# Previous input
n = int(input("Enter matrix dimension n: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(n)] for i in range(n)]

# Process
def trace_Matrix(m):
    if not m or any(len(row) != len(m) for row in m):
        raise ValueError("Trace requires a non-empty square matrix")
    return sum(m[i][i] for i in range(len(m)))

# Post process
try:
    print("Trace of matrix:", trace_Matrix(m))
except Exception as e:
    print("Cannot compute trace:", e)
