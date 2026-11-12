# Previous input
print("First 4x4matrix")
n11 = int(input("Enter first number: "))
n12 = int(input("Enter second number: "))
n13 = int(input("Enter third number: "))
n14 = int(input("Enter fourth number: "))

print("Second 4x4 matrix")
n21 = int(input("Enter first number: "))
n22 = int(input("Enter second number: "))
n23 = int(input("Enter third number: "))
n24 = int(input("Enter fourth number: "))
# Process
def add_matrices(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
# Post process
print("The sum of the two matrices is:", add_matrices([[n11, n12, n13, n14], [n21, n22, n23, n24]], [[n21, n22, n23, n24], [n11, n12, n13, n14]]))

