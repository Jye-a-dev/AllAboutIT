# Previous input
domain = [int(x.strip()) for x in input("Enter domain elements (integers, comma-separated): ").split(",") if x.strip()]

# Process
def exists_One(predicate, domain):
    return any(predicate(x) for x in domain)

# Post process
print("Existential quantification result (x > 0):", exists_One(lambda x: x > 0, domain))
