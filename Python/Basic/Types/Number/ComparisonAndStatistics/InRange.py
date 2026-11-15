# Previous input
n = float(input("Enter number to check: "))
start = float(input("Enter start of range: "))
end = float(input("Enter end of range: "))

# Process
def in_Range(n, start, end):
    low, high = sorted((start, end))
    return low <= n <= high

# Post process
print("The number is in range:", in_Range(n, start, end))
