# Previous input
x = int(input("Enter input parameter x: "))

# Process
def mu_Minimization(func, x, max_bound=1000):
    for y in range(max_bound):
        if func(x, y) == 0:
            return y
    return None

# Post process
print("Minimal y such that func(x, y) == 0:", mu_Minimization(lambda a, b: 0 if a == b * b else 1, x))
