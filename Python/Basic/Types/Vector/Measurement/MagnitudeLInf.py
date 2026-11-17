# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]

# Process
def magnitude_L_Inf(v):
    if not v:
        return 0.0
    return max(abs(x) for x in v)

# Post process
print("Chebyshev magnitude (L_inf):", magnitude_L_Inf(v))
