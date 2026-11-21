# Previous input
p = input("Enter truth value of P (True/False): ").strip().lower() in ("true", "1", "t")
q = input("Enter truth value of Q (True/False): ").strip().lower() in ("true", "1", "t")

# Process
def logical_Iff(p, q):
    return bool(p) == bool(q)

# Post process
print("Logical biconditional (P <-> Q):", logical_Iff(p, q))
