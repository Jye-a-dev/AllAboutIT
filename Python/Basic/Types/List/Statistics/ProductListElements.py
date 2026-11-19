# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def product_List_Elements(a):
    if not a:
        return 0.0
    prod = 1.0
    for x in a:
        prod *= x
    return prod

# Post process
print("Product of list elements:", product_List_Elements(a))
