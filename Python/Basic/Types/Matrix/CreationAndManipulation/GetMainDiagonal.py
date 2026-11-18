# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def get_Main_Diagonal(m):
    if not m:
        return []
    limit = min(len(m), len(m[0]))
    return [m[i][i] for i in range(limit)]

# Post process
print("Main diagonal elements:", get_Main_Diagonal(m))
