# Previous input
raw_input = input("Enter numbers separated by space: ")
nums = [float(x) for x in raw_input.split()]

# Process
def Average_N_Numbers(*numbers):
    if not numbers:
        raise ValueError("At least one number is required.")
    return sum(numbers) / len(numbers)

# Post process
print("The average is:", Average_N_Numbers(*nums))
