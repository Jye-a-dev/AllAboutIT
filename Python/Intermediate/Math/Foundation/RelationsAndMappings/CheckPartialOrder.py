# Previous input
domain = [x.strip() for x in input("Enter domain elements (comma-separated): ").split(",") if x.strip()]
n_rel = int(input("Enter number of relation pairs: "))
relation = []
for _ in range(n_rel):
    pair = [x.strip() for x in input("Enter pair (a, b): ").split(",") if x.strip()]
    relation.append((pair[0], pair[1]))

# Process
def is_Partial_Order(relation, domain):
    rel_set = set(relation)
    # Reflexive
    if not all((x, x) in rel_set for x in domain):
        return False
    # Antisymmetric
    for (a, b) in rel_set:
        if (b, a) in rel_set and a != b:
            return False
    # Transitive
    for (a, b) in rel_set:
        for (c, d) in rel_set:
            if b == c and (a, d) not in rel_set:
                return False
    return True

# Post process
print("Is partial order relation:", is_Partial_Order(relation, domain))
