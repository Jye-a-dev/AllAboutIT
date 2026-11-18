# Previous input
print("Matrix (2x2)")
n11 = int(input("Enter first number: "))
n12 = int(input("Enter second number: "))
n21 = int(input("Enter third number: "))
n22 = int(input("Enter fourth number: "))
m = [[n11, n12], [n21, n22]]

# Process
def inverse_2x2(m):
    if len(m) != 2 or len(m[0]) != 2 or len(m[1]) != 2:
        raise ValueError("Matrix must be 2x2")
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    if abs(det) < 1e-12:
        raise ValueError("Matrix is singular and cannot be inverted")
    return [
        [m[1][1] / det, -m[0][1] / det],
        [-m[1][0] / det, m[0][0] / det]
    ]

# Post process
try:
    print("Inverse of 2x2 matrix:", inverse_2x2(m))
except Exception as e:
    print("Cannot invert 2x2 matrix:", e)
