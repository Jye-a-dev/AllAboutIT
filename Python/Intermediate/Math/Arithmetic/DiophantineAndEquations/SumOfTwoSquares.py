import math

# Previous input
n = int(input("Enter non-negative integer n: "))

# Process
def find_Sum_Of_Two_Squares(n):
    if n < 0:
        return None
    a = 0
    while a * a * 2 <= n:
        b_sq = n - a * a
        b = math.isqrt(b_sq)
        if b * b == b_sq:
            return (a, b)
        a += 1
    return None

# Post process
print("Two squares representation (a, b):", find_Sum_Of_Two_Squares(n))
