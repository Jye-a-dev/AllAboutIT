# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def rotate_90_Clockwise(m):
    if not m or len(m) == 0:
        return []
    return [[m[row][col] for row in range(len(m) - 1, -1, -1)] for col in range(len(m[0]))]

# Post process
print("Rotated 90 degrees clockwise:", rotate_90_Clockwise(m))
