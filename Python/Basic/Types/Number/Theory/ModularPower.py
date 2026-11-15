# Previous input
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
mod = int(input("Enter modulus: "))

# Process
def Modular_Power(base, exp, mod):
    return pow(base, exp, mod)

# Post process
print("The modular power result is:", Modular_Power(base, exp, mod))
