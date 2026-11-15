# Previous input
raw_input = input("Enter numbers separated by space: ")
nums = [float(x) for x in raw_input.split()]

# Process
def Min_N_Numbers(*numbers):
    if not numbers:
        raise ValueError("At least one number is required.")
    return min(numbers)

# Post process
print("The minimum number is:", Min_N_Numbers(*nums))
