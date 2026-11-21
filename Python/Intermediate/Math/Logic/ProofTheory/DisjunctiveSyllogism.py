# Previous input
p_or_q = input("P or Q holds (True/False): ").strip().lower() in ("true", "1", "t")
not_p = input("not P holds (True/False): ").strip().lower() in ("true", "1", "t")

# Process
def apply_Disjunctive_Syllogism(p_or_q, not_p):
    if p_or_q and not_p:
        return True
    return None

# Post process
print("Deduced Q by Disjunctive Syllogism:", apply_Disjunctive_Syllogism(p_or_q, not_p))
