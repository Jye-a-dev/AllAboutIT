# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def find_Least_Frequent(a):
    if not a:
        return None
    freq = {}
    for item in a:
        freq[item] = freq.get(item, 0) + 1
    return min(freq, key=freq.get)

# Post process
print("The least frequent element is:", find_Least_Frequent(a))
