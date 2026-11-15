# Previous input
a = int(input("Enter the number to check: "))

# Process
def is_Integer(a):
    return isinstance(a, int)

# Post process
if is_Integer(a):
    print("The number is an integer:", a)
else:
    print("The number is not an integer:", a)

print("The result of is_Integer(a) is:", is_Integer(a))
