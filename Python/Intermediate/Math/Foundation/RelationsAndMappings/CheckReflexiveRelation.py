# Previous input
domain = [x.strip() for x in input("Enter domain elements (comma-separated): ").split(",") if x.strip()]
n_rel = int(input("Enter number of relation pairs: "))
relation = []
for _ in range(n_rel):
    pair = [x.strip() for x in input("Enter pair (a, b): ").split(",") if x.strip()]
    relation.append((pair[0], pair[1]))

# Process
def is_Reflexive_Relation(relation, domain):
    rel_set = set(relation)
    return all((x, x) in rel_set for x in domain)

# Post process
print("Is reflexive relation:", is_Reflexive_Relation(relation, domain))
