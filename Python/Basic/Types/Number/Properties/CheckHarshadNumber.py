# Previous input
n = int(input("Enter positive integer to check: "))

# Process
def is_Harshad(n):
    if n <= 0:
        return False
    digit_sum = sum(int(d) for d in str(n))
    return n % digit_sum == 0

# Post process
if is_Harshad(n):
    print("The number is a Harshad number:", n)
else:
    print("The number is not a Harshad number:", n)

print("The result of is_Harshad(n) is:", is_Harshad(n))
