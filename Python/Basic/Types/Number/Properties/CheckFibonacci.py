# Previous input

a = int(input("Enter the number to check: "))

# Process
def is_Fibonacci(a):
    if a == 0 or a == 1:
        return True
    prev, curr = 0, 1
    while curr < a:
        prev, curr = curr, prev + curr
    return curr == a

# Post process
if is_Fibonacci(a):
    print("The number is a Fibonacci number:", a)
else:
    print("The number is not a Fibonacci number:", a)

print("The result of is_Fibonacci(a) is:", is_Fibonacci(a)) 

