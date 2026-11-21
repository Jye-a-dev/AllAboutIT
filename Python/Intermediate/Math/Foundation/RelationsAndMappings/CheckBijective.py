# Previous input
domain = [x.strip() for x in input("Enter domain elements (comma-separated): ").split(",") if x.strip()]
codomain = [x.strip() for x in input("Enter codomain elements (comma-separated): ").split(",") if x.strip()]
n_map = int(input("Enter number of mappings: "))
mapping = {}
for _ in range(n_map):
    pair = [x.strip() for x in input("Enter mapping (x, y): ").split(",") if x.strip()]
    mapping[pair[0]] = pair[1]

# Process
def is_Bijective(mapping, domain, codomain):
    m_dict = dict(mapping) if not isinstance(mapping, dict) else mapping
    if set(m_dict.keys()) != set(domain):
        return False
    if not set(codomain).issubset(set(m_dict.values())):
        return False
    values = list(m_dict.values())
    return len(values) == len(set(values))

# Post process
print("Is bijective:", is_Bijective(mapping, domain, codomain))
