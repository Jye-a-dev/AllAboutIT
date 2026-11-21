# Previous input
n_rel = int(input("Enter number of relation pairs: "))
relation = []
for _ in range(n_rel):
    pair = [x.strip() for x in input("Enter pair (a, b): ").split(",") if x.strip()]
    relation.append((pair[0], pair[1]))

# Process
def is_Antisymmetric_Relation(relation):
    rel_set = set(relation)
    for (a, b) in rel_set:
        if (b, a) in rel_set and a != b:
            return False
    return True

# Post process
print("Is antisymmetric relation:", is_Antisymmetric_Relation(relation))
