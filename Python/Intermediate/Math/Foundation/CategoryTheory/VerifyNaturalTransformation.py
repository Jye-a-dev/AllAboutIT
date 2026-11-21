# Previous input
nt_name = input("Enter natural transformation name: ").strip()

# Process
def is_Natural_Transformation(cat_c, cat_d, functor_f, functor_g, components):
    # components: {obj: eta_obj}
    # Naturality square for every morphism f: A -> B in cat_c:
    # eta_B o F(f) == G(f) o eta_A in cat_d
    mor_c = cat_c.get("morphisms", {})
    comp_d = cat_d.get("composition", {})
    for f, (src, dst) in mor_c.items():
        eta_src = components.get(src)
        eta_dst = components.get(dst)
        f_f = functor_f.get("mor_map", {}).get(f)
        g_f = functor_g.get("mor_map", {}).get(f)
        left = comp_d.get((f_f, eta_dst))
        right = comp_d.get((eta_src, g_f))
        if left != right:
            return False
    return True

# Post process
print("Is valid natural transformation:", is_Natural_Transformation({'morphisms': {'id_A': ('A', 'A')}}, {'composition': {('id_X', 'eta_A'): 'eta_A', ('eta_A', 'id_X'): 'eta_A'}}, {'mor_map': {'id_A': 'id_X'}}, {'mor_map': {'id_A': 'id_X'}}, {'A': 'eta_A'}))
