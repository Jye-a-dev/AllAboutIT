# Previous input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Process
def rotate_180(m):
    return [row[::-1] for row in m[::-1]]

# Post process
print("Rotated 180 degrees:", rotate_180(m))
