# Previous input
a = [x.strip() for x in input("Enter list elements (comma-separated): ").split(",") if x.strip()]

# Process
def is_All_Numeric_List(a):
    if not a:
        return False
    for item in a:
        if isinstance(item, (int, float, complex)):
            continue
        try:
            float(item)
        except (ValueError, TypeError):
            return False
    return True

# Post process
print("All elements in the list are numeric:", is_All_Numeric_List(a))
