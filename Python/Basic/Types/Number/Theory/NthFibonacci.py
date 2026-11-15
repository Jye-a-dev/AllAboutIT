# Previous input
n = int(input("Enter index n for Fibonacci number: "))

# Process
def Nth_Fibonacci(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Post process
print("The Fibonacci number at index", n, "is:", Nth_Fibonacci(n))
