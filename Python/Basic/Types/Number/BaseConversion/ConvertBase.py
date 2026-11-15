# Previous input
num_str = input("Enter number string: ")
from_base = int(input("Enter from base (2-36): "))
to_base = int(input("Enter to base (2-36): "))

# Process
def convert_Base(num_str, from_base, to_base):
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        raise ValueError("Bases must be between 2 and 36 inclusive.")
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = num_str.strip()
    is_neg = s.startswith("-")
    if is_neg or s.startswith("+"):
        s = s[1:]
    
    decimal_val = int(s, from_base)
    if decimal_val == 0:
        return "0"
    
    res = []
    while decimal_val > 0:
        res.append(digits[decimal_val % to_base])
        decimal_val //= to_base
    
    converted = "".join(reversed(res))
    return f"-{converted}" if is_neg else converted

# Post process
print(f"The number {num_str} in base {to_base} is:", convert_Base(num_str, from_base, to_base))
