# Previous input
domain = [x.strip() for x in input("Enter domain elements (comma-separated): ").split(",") if x.strip()]
n_rel = int(input("Enter number of relation pairs: "))
relation = []
for _ in range(n_rel):
    pair = [x.strip() for x in input("Enter pair (a, b): ").split(",") if x.strip()]
    relation.append((pair[0], pair[1]))

# Process
def get_Equivalence_Classes(relation, domain):
    rel_set = set(relation)
    visited = set()
    classes = []
    for elem in domain:
        if elem not in visited:
            eq_class = {b for (a, b) in rel_set if a == elem} | {elem}
            visited |= eq_class
            classes.append(sorted(list(eq_class)))
    return classes

# Post process
print("Equivalence classes (quotient set A / ~):", get_Equivalence_Classes(relation, domain))
