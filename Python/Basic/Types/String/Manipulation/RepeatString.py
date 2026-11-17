# Previous input
a = input("Enter the string: ")
n = int(input("Enter number of repetitions: "))

# Process
def repeat_String(a, n):
    return a * n if n > 0 else ""

# Post process
print("Repeated string:", repeat_String(a, n))
