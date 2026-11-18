# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def flip_Vertical(m):
    return m[::-1]

# Post process
print("Vertically flipped matrix:", flip_Vertical(m))
