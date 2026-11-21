# Previous input
p = input("Enter truth value of P (True/False): ").strip().lower() in ("true", "1", "t")
q = input("Enter truth value of Q (True/False): ").strip().lower() in ("true", "1", "t")

# Process
def logical_Nand(p, q):
    return not (bool(p) and bool(q))

# Post process
print("Logical NAND:", logical_Nand(p, q))
