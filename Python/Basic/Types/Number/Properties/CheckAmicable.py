# Previous input
a = int(input("Enter the first number to check: "))
b = int(input("Enter the second number to check: "))

# Process
def is_amicable_numbers(a, b):
    # Calculate the sum of proper divisors for each number
    sum_a = sum(i for i in range(1, a) if a % i == 0)
    sum_b = sum(i for i in range(1, b) if b % i == 0)
    # Check if the sums are equal to the other number
    return sum_a == b and sum_b == a

# Post process
if is_amicable_numbers(a, b):
    print("The numbers are amicable:", a, b)
else:
    print("The numbers are not amicable:", a, b)

print("The result of is_amicable_numbers(a, b) is:", is_amicable_numbers(a, b))
   