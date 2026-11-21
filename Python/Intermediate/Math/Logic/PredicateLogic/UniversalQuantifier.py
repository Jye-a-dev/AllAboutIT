# Previous input
domain = [int(x.strip()) for x in input("Enter domain elements (integers, comma-separated): ").split(",") if x.strip()]

# Process
def for_All(predicate, domain):
    return all(predicate(x) for x in domain)

# Post process
print("Universal quantification result (x > 0):", for_All(lambda x: x > 0, domain))
