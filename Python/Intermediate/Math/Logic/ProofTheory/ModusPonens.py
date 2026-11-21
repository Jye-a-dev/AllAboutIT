# Previous input
p = input("Premise P is asserted (True/False): ").strip().lower() in ("true", "1", "t")
p_implies_q = input("Premise P -> Q is asserted (True/False): ").strip().lower() in ("true", "1", "t")

# Process
def apply_Modus_Ponens(p, p_implies_q):
    if p and p_implies_q:
        return True
    return None

# Post process
print("Deduced Q by Modus Ponens:", apply_Modus_Ponens(p, p_implies_q))
