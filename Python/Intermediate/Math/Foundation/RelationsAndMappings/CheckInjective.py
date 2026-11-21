# Previous input
n_map = int(input("Enter number of mappings: "))
mapping = {}
for _ in range(n_map):
    pair = [x.strip() for x in input("Enter mapping (x, y): ").split(",") if x.strip()]
    mapping[pair[0]] = pair[1]

# Process
def is_Injective(mapping):
    m_dict = dict(mapping) if not isinstance(mapping, dict) else mapping
    values = list(m_dict.values())
    return len(values) == len(set(values))

# Post process
print("Is injective (one-to-one):", is_Injective(mapping))
