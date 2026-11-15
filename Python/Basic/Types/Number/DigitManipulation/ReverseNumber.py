# Previous input
n = int(input("Enter integer number: "))

# Process
def reverse_Number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])

# Post process
print("The reversed number is:", reverse_Number(n))
