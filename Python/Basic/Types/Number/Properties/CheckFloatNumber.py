# Previous input
val = input("Enter value or number to check: ")
try:
    if "." in val:
        n = float(val)
    else:
        n = int(val)
except ValueError:
    n = val

# Process
def is_Float(n):
    return isinstance(n, float)

# Post process
if is_Float(n):
    print("The value is a float:", n)
else:
    print("The value is not a float:", n)

print("The result of is_Float(n) is:", is_Float(n))
