# Previous input

a = int(input("Enter the number to check: "))

# Process
def is_armstrong_number(a):
    # Convert the number to a string to easily iterate over each digit
    str_a = str(a)
    num_digits = len(str_a)
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_a)
    return sum_of_powers == a

# Post process
if is_armstrong_number(a):
    print("The number is an Armstrong number:", a)
else:
    print("The number is not an Armstrong number:", a)

print("The result of is_armstrong_number(a) is:", is_armstrong_number(a)) 
