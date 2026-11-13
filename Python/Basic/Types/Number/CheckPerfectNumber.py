# Previous input

a = int(input("Enter the number to check: "))

# Process
def is_perfect_number(a):
    if a < 2:
        return False
    divisors_sum = 1
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            divisors_sum += i
            if i != a // i:
                divisors_sum += a // i
    return divisors_sum == a

# Post process
if is_perfect_number(a):
    print("The number is a perfect number:", a)
else:
    print("The number is not a perfect number:", a)

print("The result of is_perfect_number(a) is:", is_perfect_number(a)) 
