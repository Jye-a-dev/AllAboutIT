# Previous input
n = int(input("Enter non-negative integer ordinal index n: "))

# Process
def construct_Von_Neumann_Ordinal(n):
    if n < 0:
        raise ValueError("Ordinal index must be non-negative")
    ordinals = [()]
    for i in range(1, n + 1):
        ordinals.append(tuple(ordinals[:i]))
    return ordinals[n]

# Post process
print("Von Neumann ordinal structure:", construct_Von_Neumann_Ordinal(n))
