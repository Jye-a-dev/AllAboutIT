import math

# Previous input
z = int(input("Enter non-negative Cantor index z: "))

# Process
def inverse_Cantor_Pairing(z):
    if z < 0:
        raise ValueError("Index must be non-negative")
    w = (math.isqrt(8 * z + 1) - 1) // 2
    t = (w * (w + 1)) // 2
    k2 = z - t
    k1 = w - k2
    return (k1, k2)

# Post process
print("Inverse Cantor pair (k1, k2):", inverse_Cantor_Pairing(z))
