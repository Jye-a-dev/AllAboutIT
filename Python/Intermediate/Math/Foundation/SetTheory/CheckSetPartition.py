# Previous input
original_set = [x.strip() for x in input("Enter elements of original set (comma-separated): ").split(",") if x.strip()]
n_blocks = int(input("Enter number of subset blocks: "))
subsets = []
for i in range(n_blocks):
    subsets.append([x.strip() for x in input(f"Enter block {i + 1} elements: ").split(",") if x.strip()])

# Process
def is_Valid_Partition(subsets, original_set):
    if not subsets:
        return len(original_set) == 0
    orig = set(original_set)
    seen = set()
    for block in subsets:
        b_set = set(block)
        if len(b_set) == 0:
            return False
        if seen & b_set:
            return False
        seen |= b_set
    return seen == orig

# Post process
print("Is valid partition:", is_Valid_Partition(subsets, original_set))
