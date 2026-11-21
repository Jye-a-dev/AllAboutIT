# Previous input
n_f = int(input("Enter number of pairs in mapping f: "))
f = {}
for _ in range(n_f):
    pair = [x.strip() for x in input("Enter pair for f (x, y): ").split(",") if x.strip()]
    f[pair[0]] = pair[1]
n_g = int(input("Enter number of pairs in mapping g: "))
g = {}
for _ in range(n_g):
    pair = [x.strip() for x in input("Enter pair for g (y, z): ").split(",") if x.strip()]
    g[pair[0]] = pair[1]

# Process
def compose_Mappings(f, g):
    f_dict = dict(f) if not isinstance(f, dict) else f
    g_dict = dict(g) if not isinstance(g, dict) else g
    res = {}
    for x, y in f_dict.items():
        if y in g_dict:
            res[x] = g_dict[y]
    return res

# Post process
print("Composed mapping (g o f):", compose_Mappings(f, g))
