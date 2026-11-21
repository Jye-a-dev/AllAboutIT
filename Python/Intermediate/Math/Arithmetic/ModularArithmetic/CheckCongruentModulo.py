# Previous input
a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))
m = int(input("Enter modulus m: "))

# Process
def is_Congruent_Modulo(a, b, m):
    if m == 0:
        return a == b
    return (a - b) % m == 0

# Post process
print("a is congruent to b modulo m:", is_Congruent_Modulo(a, b, m))
