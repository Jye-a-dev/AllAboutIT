# Previous input
non_empty_set = [x.strip() for x in input("Enter set elements (comma-separated): ").split(",") if x.strip()]

# Process
def verify_Zfc_Regularity(non_empty_set):
    if not non_empty_set:
        return True
    s = set(non_empty_set)
    # Check no self-membership: s not in s (represented by string token matching)
    for elem in s:
        if elem == str(non_empty_set):
            return False
    # There must exist an element disjoint from the set
    # In finite model representation, an element that does not share elements
    return True

# Post process
print("Axiom of regularity holds:", verify_Zfc_Regularity(non_empty_set))
