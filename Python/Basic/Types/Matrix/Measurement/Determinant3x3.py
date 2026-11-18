# Previous input
print("Matrix (3x3)")
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(3)] for i in range(3)]

# Process
def determinant_3x3(m):
    if len(m) != 3 or any(len(row) != 3 for row in m):
        raise ValueError("Matrix must be 3x3")
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )

# Post process
try:
    print("Determinant of 3x3 matrix:", determinant_3x3(m))
except Exception as e:
    print("Cannot compute 3x3 determinant:", e)
