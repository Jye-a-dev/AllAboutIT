# Previous input
domain = [int(x.strip()) for x in input("Enter domain elements (integers, comma-separated): ").split(",") if x.strip()]

# Process
def exists_Unique(predicate, domain):
    count = 0
    for x in domain:
        if predicate(x):
            count += 1
            if count > 1:
                return False
    return count == 1

# Post process
print("Unique existential quantification result (x == 0):", exists_Unique(lambda x: x == 0, domain))
