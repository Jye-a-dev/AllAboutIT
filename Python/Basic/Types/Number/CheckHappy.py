# Previous input

a = int(input("Enter the number to check: "))

# Process
def is_happy(a):
    def get_sum_of_squares(n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    seen = set()
    while a != 1 and a not in seen:
        seen.add(a)
        a = get_sum_of_squares(a)
    return a == 1

# Post process
if is_happy(a):
    print("The number is a happy number:", a)
else:
    print("The number is not a happy number:", a)

print("The result of is_happy(a) is:", is_happy(a)) 
