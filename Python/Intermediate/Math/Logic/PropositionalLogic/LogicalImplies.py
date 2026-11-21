# Previous input
p = input("Enter truth value of P (True/False): ").strip().lower() in ("true", "1", "t")
q = input("Enter truth value of Q (True/False): ").strip().lower() in ("true", "1", "t")

# Process
def logical_Implies(p, q):
    return (not p) or bool(q)

# Post process
print("Logical implication (P -> Q):", logical_Implies(p, q))
