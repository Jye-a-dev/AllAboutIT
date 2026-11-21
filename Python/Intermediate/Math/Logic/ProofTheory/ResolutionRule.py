# Previous input
c1 = [x.strip() for x in input("Enter literals in clause 1 (e.g. p, ~q): ").split(",") if x.strip()]
c2 = [x.strip() for x in input("Enter literals in clause 2 (e.g. q, r): ").split(",") if x.strip()]

# Process
def resolve_Clauses(c1, c2):
    s1 = set(c1)
    s2 = set(c2)
    resolvents = []
    for lit in s1:
        neg = lit[1:] if lit.startswith("~") else f"~{lit}"
        if neg in s2:
            res = (s1 - {lit}) | (s2 - {neg})
            resolvents.append(sorted(list(res)))
    return resolvents

# Post process
print("Resolvent clauses:", resolve_Clauses(c1, c2))
