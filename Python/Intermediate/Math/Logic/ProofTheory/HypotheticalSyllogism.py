# Previous input
p_implies_q = input("P -> Q holds (True/False): ").strip().lower() in ("true", "1", "t")
q_implies_r = input("Q -> R holds (True/False): ").strip().lower() in ("true", "1", "t")

# Process
def apply_Hypothetical_Syllogism(p_implies_q, q_implies_r):
    if p_implies_q and q_implies_r:
        return True
    return None

# Post process
print("Deduced P -> R by Hypothetical Syllogism:", apply_Hypothetical_Syllogism(p_implies_q, q_implies_r))
