# Previous input
n_rel = int(input("Enter number of relation pairs: "))
relation = []
for _ in range(n_rel):
    pair = [x.strip() for x in input("Enter pair (a, b): ").split(",") if x.strip()]
    relation.append((pair[0], pair[1]))

# Process
def transitive_Closure_Relation(relation):
    closure = set(relation)
    changed = True
    while changed:
        changed = False
        to_add = set()
        for (a, b) in closure:
            for (c, d) in closure:
                if b == c and (a, d) not in closure:
                    to_add.add((a, d))
        if to_add:
            closure |= to_add
            changed = True
    return sorted(list(closure))

# Post process
print("Transitive closure:", transitive_Closure_Relation(relation))
