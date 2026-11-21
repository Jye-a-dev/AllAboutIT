# Previous input
not_q = input("Premise not Q is asserted (True/False): ").strip().lower() in ("true", "1", "t")
p_implies_q = input("Premise P -> Q is asserted (True/False): ").strip().lower() in ("true", "1", "t")

# Process
def apply_Modus_Tollens(not_q, p_implies_q):
    if not_q and p_implies_q:
        return True
    return None

# Post process
print("Deduced not P by Modus Tollens:", apply_Modus_Tollens(not_q, p_implies_q))
