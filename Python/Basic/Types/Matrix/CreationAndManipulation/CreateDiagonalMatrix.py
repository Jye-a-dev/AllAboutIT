# Previous input
n = int(input("Enter number of diagonal elements: "))
diag_elements = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]

# Process
def create_Diagonal_Matrix(diag_elements):
    n = len(diag_elements)
    return [[diag_elements[i] if i == j else 0 for j in range(n)] for i in range(n)]

# Post process
print("Diagonal matrix:", create_Diagonal_Matrix(diag_elements))
