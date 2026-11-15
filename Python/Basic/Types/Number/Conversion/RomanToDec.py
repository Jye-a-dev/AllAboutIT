# Previous input
n1 = input("Enter Roman number: ")

# Process
def from_Roman_Decimal(a):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(a):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

# Post process
print("The decimal representation is:", from_Roman_Decimal(n1))
