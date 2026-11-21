# Previous input
n_rel = int(input("Enter number of relation pairs: "))
relation = []
for _ in range(n_rel):
    pair = [x.strip() for x in input("Enter pair (a, b): ").split(",") if x.strip()]
    relation.append((pair[0], pair[1]))

# Process
def is_Symmetric_Relation(relation):
    rel_set = set(relation)
    return all((b, a) in rel_set for (a, b) in rel_set)

# Post process
print("Is symmetric relation:", is_Symmetric_Relation(relation))
