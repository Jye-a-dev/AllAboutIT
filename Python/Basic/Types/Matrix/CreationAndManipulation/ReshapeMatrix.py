# Previous input
rows = int(input("Enter original rows: "))
cols = int(input("Enter original cols: "))
m = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
new_rows = int(input("Enter new rows: "))
new_cols = int(input("Enter new cols: "))

# Process
def reshape_Matrix(m, new_rows, new_cols):
    flat = [val for row in m for val in row]
    if len(flat) != new_rows * new_cols:
        raise ValueError(f"Cannot reshape matrix of size {len(flat)} into ({new_rows}, {new_cols})")
    return [[flat[i * new_cols + j] for j in range(new_cols)] for i in range(new_rows)]

# Post process
try:
    print("Reshaped matrix:", reshape_Matrix(m, new_rows, new_cols))
except Exception as e:
    print("Cannot reshape matrix:", e)
