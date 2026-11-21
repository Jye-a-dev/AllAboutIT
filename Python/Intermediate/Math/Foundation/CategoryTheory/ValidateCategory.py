# Previous input
objects = [x.strip() for x in input("Enter objects (comma-separated): ").split(",") if x.strip()]

# Process
def is_Valid_Category(objects, morphisms, identities, composition):
    obj_set = set(objects)
    # Check identities exist for all objects
    for obj in obj_set:
        if obj not in identities or identities[obj] not in morphisms:
            return False
    # Check composition associativity: (h o g) o f == h o (g o f)
    for (f, g), gf in composition.items():
        for (g_cand, h), hg in composition.items():
            if g_cand == gf:
                # h o (g o f) = h o gf
                left = composition.get((gf, h))
                right_intermediate = composition.get((g, h))
                if right_intermediate:
                    right = composition.get((f, right_intermediate))
                    if left != right:
                        return False
    # Check identity laws
    for m in morphisms:
        for obj in obj_set:
            id_m = identities[obj]
            if (id_m, m) in composition and composition[(id_m, m)] != m:
                return False
            if (m, id_m) in composition and composition[(m, id_m)] != m:
                return False
    return True

# Post process
print("Is valid category:", is_Valid_Category(objects, {'id_A': ('A', 'A')}, {'A': 'id_A'}, {('id_A', 'id_A'): 'id_A'} if objects else {}))
