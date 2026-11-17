# Previous input
a = input("Enter the first string: ")
b = input("Enter the second string: ")

# Process
def hamming_Distance(a, b):
    if len(a) != len(b):
        raise ValueError("Strings must be of equal length to calculate Hamming distance")
    return sum(1 for c1, c2 in zip(a, b) if c1 != c2)

# Post process
try:
    print("Hamming distance:", hamming_Distance(a, b))
except ValueError as e:
    print("Hamming distance error:", e)
