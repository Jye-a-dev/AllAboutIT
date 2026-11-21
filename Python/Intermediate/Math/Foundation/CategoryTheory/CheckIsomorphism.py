# Previous input
f = input("Enter morphism f: ").strip()

# Process
def is_Isomorphism_Morphism(f, morphisms, composition_table, identities):
    # Check if there exists g such that g o f = id_A and f o g = id_B
    id_values = set(identities.values())
    for g in morphisms:
        g_o_f = composition_table.get((f, g))
        f_o_g = composition_table.get((g, f))
        if g_o_f in id_values and f_o_g in id_values:
            return True
    return False

# Post process
print("Is isomorphism morphism:", is_Isomorphism_Morphism(f, [f], {(f, f): 'id_A'}, {'A': 'id_A'}))
