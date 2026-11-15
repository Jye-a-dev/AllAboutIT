# Previous input
num = float(input("Enter number: "))
decimals_input = input("Enter number of decimal places (default 0): ")
dec = int(decimals_input) if decimals_input.strip() else 0

# Process
def round_Number(n, decimals=0):
    return round(n, decimals) if decimals > 0 else round(n)

# Post process
print("The rounded number is:", round_Number(num, dec))
