# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
n = int(input("Enter number of elements to take: ").strip())

# Process
def take_First_N(a, n):
    return a[:max(0, n)]

# Post process
print("First elements taken:", take_First_N(a, n))
