# Previous input
f = input("Enter morphism f: ").strip()

# Process
def is_Monomorphism(f, morphisms, composition_table):
    # Left-cancellative: f o g1 == f o g2 implies g1 == g2
    for g1 in morphisms:
        for g2 in morphisms:
            fg1 = composition_table.get((g1, f))
            fg2 = composition_table.get((g2, f))
            if fg1 is not None and fg2 is not None and fg1 == fg2:
                if g1 != g2:
                    return False
    return True

# Post process
print("Is monomorphism (left-cancellative):", is_Monomorphism(f, [f], {(f, f): f}))
