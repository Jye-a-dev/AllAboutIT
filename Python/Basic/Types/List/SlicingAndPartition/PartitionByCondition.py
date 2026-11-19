# Previous input
a = [int(x.strip()) for x in input("Enter integers (comma-separated): ").split(",") if x.strip()]

# Process
def partition_Even_Odd(a):
    evens = [x for x in a if x % 2 == 0]
    odds = [x for x in a if x % 2 != 0]
    return evens, odds

# Post process
print("Partitioned (even, odd):", partition_Even_Odd(a))
