# Previous input
n_rel = int(input("Enter number of relation pairs: "))
relation = []
for _ in range(n_rel):
    pair = [x.strip() for x in input("Enter pair (a, b): ").split(",") if x.strip()]
    relation.append((pair[0], pair[1]))

# Process
def is_Transitive_Relation(relation):
    rel_set = set(relation)
    for (a, b) in rel_set:
        for (c, d) in rel_set:
            if b == c and (a, d) not in rel_set:
                return False
    return True

# Post process
print("Is transitive relation:", is_Transitive_Relation(relation))
