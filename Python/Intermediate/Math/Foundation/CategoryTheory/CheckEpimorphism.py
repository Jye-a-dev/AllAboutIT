# Previous input
f = input("Enter morphism f: ").strip()

# Process
def is_Epimorphism(f, morphisms, composition_table):
    # Right-cancellative: g1 o f == g2 o f implies g1 == g2
    for g1 in morphisms:
        for g2 in morphisms:
            g1f = composition_table.get((f, g1))
            g2f = composition_table.get((f, g2))
            if g1f is not None and g2f is not None and g1f == g2f:
                if g1 != g2:
                    return False
    return True

# Post process
print("Is epimorphism (right-cancellative):", is_Epimorphism(f, [f], {(f, f): f}))
