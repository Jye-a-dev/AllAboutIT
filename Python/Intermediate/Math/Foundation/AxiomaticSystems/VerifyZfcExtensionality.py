# Previous input
set_a = [x.strip() for x in input("Enter elements of set A (comma-separated): ").split(",") if x.strip()]
set_b = [x.strip() for x in input("Enter elements of set B (comma-separated): ").split(",") if x.strip()]

# Process
def verify_Zfc_Extensionality(set_a, set_b):
    sa = set(set_a)
    sb = set(set_b)
    # Axiom: forall x (x in A <=> x in B) => A == B
    elements_match = (sa == sb)
    return elements_match

# Post process
print("Extensionality verified:", verify_Zfc_Extensionality(set_a, set_b))
