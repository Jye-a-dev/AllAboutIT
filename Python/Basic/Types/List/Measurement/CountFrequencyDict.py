# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]

# Process
def count_Frequency_Dict(a):
    freq = {}
    for item in a:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Post process
print("Element frequency dictionary:", count_Frequency_Dict(a))
