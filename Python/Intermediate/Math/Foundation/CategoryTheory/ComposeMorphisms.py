# Previous input
f = input("Enter morphism f: ").strip()
g = input("Enter morphism g: ").strip()

# Process
def compose_Morphisms(f, g, composition_table):
    return composition_table.get((f, g))

# Post process
print("Composed morphism (g o f):", compose_Morphisms(f, g, {(f, g): f"{g}_after_{f}"}))
