# Previous input
n_map = int(input("Enter number of mappings: "))
mapping = {}
for _ in range(n_map):
    pair = [x.strip() for x in input("Enter mapping (x, y): ").split(",") if x.strip()]
    mapping[pair[0]] = pair[1]

# Process
def inverse_Mapping(mapping):
    m_dict = dict(mapping) if not isinstance(mapping, dict) else mapping
    values = list(m_dict.values())
    if len(values) != len(set(values)):
        return None
    return {v: k for k, v in m_dict.items()}

# Post process
print("Inverse mapping f^-1:", inverse_Mapping(mapping))
