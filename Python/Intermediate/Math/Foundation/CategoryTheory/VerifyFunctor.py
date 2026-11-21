# Previous input
f_name = input("Enter functor name: ").strip()

# Process
def is_Valid_Functor(cat_c, cat_d, obj_map, mor_map):
    # cat = {'objects': [...], 'morphisms': [...], 'identities': {obj: id}, 'composition': {(f, g): h}}
    # Check identity preservation: F(id_A) == id_F(A)
    for obj, id_c in cat_c.get("identities", {}).items():
        target_obj = obj_map.get(obj)
        id_d = cat_d.get("identities", {}).get(target_obj)
        if mor_map.get(id_c) != id_d:
            return False
    # Check composition preservation: F(g o f) == F(g) o F(f)
    for (f, g), gf in cat_c.get("composition", {}).items():
        f_f = mor_map.get(f)
        f_g = mor_map.get(g)
        f_gf = mor_map.get(gf)
        expected = cat_d.get("composition", {}).get((f_f, f_g))
        if f_gf != expected:
            return False
    return True

# Post process
print("Is valid functor:", is_Valid_Functor({'identities': {'A': 'id_A'}}, {'identities': {'X': 'id_X'}}, {'A': 'X'}, {'id_A': 'id_X'}))
