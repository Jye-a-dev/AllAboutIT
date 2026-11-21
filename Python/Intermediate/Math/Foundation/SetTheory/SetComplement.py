# Previous input
u = [x.strip() for x in input("Enter elements of universal set U: ").split(",") if x.strip()]
a = [x.strip() for x in input("Enter elements of subset A: ").split(",") if x.strip()]

# Process
def complement_Set(u, a):
    sa = set(a)
    return [x for x in dict.fromkeys(u) if x not in sa]

# Post process
print("Complement U \\ A:", complement_Set(u, a))
