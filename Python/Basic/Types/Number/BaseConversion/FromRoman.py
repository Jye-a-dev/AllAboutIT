# Previous input
s = input("Enter Roman numeral: ")

# Process
def from_Roman(roman_str):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_val = 0
    for ch in reversed(roman_str.strip().upper()):
        if ch not in roman_map:
            raise ValueError(f"Invalid Roman numeral character: {ch}")
        curr_val = roman_map[ch]
        if curr_val < prev_val:
            total -= curr_val
        else:
            total += curr_val
        prev_val = curr_val
    return total

# Post process
print("The decimal integer is:", from_Roman(s))
