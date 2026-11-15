# Previous input
from Python.Basic.Types.Number.Conversion.HexToOct import from_Hexadecimal_Octal


n1 = int(input("Enter octal number: "), 8)

# Process
def from_Octal_Hexadecimal(a):
    return hex(a)[2:]
# Post process
print("The hexadecimal representation is:", from_Octal_Hexadecimal(n1))
