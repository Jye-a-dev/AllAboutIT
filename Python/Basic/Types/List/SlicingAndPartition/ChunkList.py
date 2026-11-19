# Previous input
a = [x.strip() for x in input("Enter the list (comma-separated): ").split(",") if x.strip()]
size = int(input("Enter chunk size: ").strip())

# Process
def chunk_List(a, size):
    if size <= 0:
        return [list(a)] if a else []
    return [a[i:i + size] for i in range(0, len(a), size)]

# Post process
print("Chunked list:", chunk_List(a, size))
