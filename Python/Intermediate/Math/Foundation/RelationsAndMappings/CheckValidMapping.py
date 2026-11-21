# Previous input
domain = [x.strip() for x in input("Enter domain elements (comma-separated): ").split(",") if x.strip()]
codomain = [x.strip() for x in input("Enter codomain elements (comma-separated): ").split(",") if x.strip()]
n_map = int(input("Enter number of mappings: "))
mapping = {}
for _ in range(n_map):
    pair = [x.strip() for x in input("Enter mapping (x, y): ").split(",") if x.strip()]
    mapping[pair[0]] = pair[1]

# Process
def is_Valid_Mapping(mapping, domain, codomain):
    d_set = set(domain)
    cd_set = set(codomain)
    m_dict = dict(mapping) if not isinstance(mapping, dict) else mapping
    if set(m_dict.keys()) != d_set:
        return False
    return all(v in cd_set for v in m_dict.values())

# Post process
print("Is valid mapping:", is_Valid_Mapping(mapping, domain, codomain))
