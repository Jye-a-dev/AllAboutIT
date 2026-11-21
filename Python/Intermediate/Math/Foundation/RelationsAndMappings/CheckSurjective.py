# Previous input
codomain = [x.strip() for x in input("Enter codomain elements (comma-separated): ").split(",") if x.strip()]
n_map = int(input("Enter number of mappings: "))
mapping = {}
for _ in range(n_map):
    pair = [x.strip() for x in input("Enter mapping (x, y): ").split(",") if x.strip()]
    mapping[pair[0]] = pair[1]

# Process
def is_Surjective(mapping, codomain):
    m_dict = dict(mapping) if not isinstance(mapping, dict) else mapping
    return set(codomain).issubset(set(m_dict.values()))

# Post process
print("Is surjective (onto):", is_Surjective(mapping, codomain))
