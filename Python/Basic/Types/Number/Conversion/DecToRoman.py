# Previous input
n1 = int(input("Enter decimal number: "))

# Process
def to_Roman(a):
    # Implementation for converting decimal to Roman numerals
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""

    for value, symbol in zip(values, roman):
        while a >= value:
            result += symbol
            a -= value

    return result

# Post process
print("The Roman representation is:", to_Roman(n1))
