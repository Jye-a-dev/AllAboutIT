# Previous input
raw_input = input("Enter numbers separated by space: ")
nums = [float(x) for x in raw_input.split()]

# Process
def Max_N_Numbers(*numbers):
    if not numbers:
        raise ValueError("At least one number is required.")
    return max(numbers)

# Post process
print("The maximum number is:", Max_N_Numbers(*nums))
