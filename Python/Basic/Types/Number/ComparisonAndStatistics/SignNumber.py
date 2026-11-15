# Previous input
num = float(input("Enter number: "))

# Process
def Sign_Number(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0

# Post process
print("The sign of the number is:", Sign_Number(num))
