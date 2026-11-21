# Previous input
k1 = int(input("Enter non-negative integer k1: "))
k2 = int(input("Enter non-negative integer k2: "))

# Process
def cantor_Pairing(k1, k2):
    if k1 < 0 or k2 < 0:
        raise ValueError("Inputs must be non-negative integers")
    return ((k1 + k2) * (k1 + k2 + 1)) // 2 + k2

# Post process
print("Cantor pairing index pi(k1, k2):", cantor_Pairing(k1, k2))
