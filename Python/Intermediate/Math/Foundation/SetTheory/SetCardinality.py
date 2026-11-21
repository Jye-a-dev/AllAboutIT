# Previous input
s = [x.strip() for x in input("Enter set elements (comma-separated): ").split(",") if x.strip()]

# Process
def get_Cardinality(s):
    return len(set(s))

# Post process
print("Cardinality of set |S|:", get_Cardinality(s))
