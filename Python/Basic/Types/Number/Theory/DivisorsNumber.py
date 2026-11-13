# Previous input
a = int(input("Enter the number to calculate divisors for: "))
# Process
def Divisor_Number(a):
    if a <= 0:
        return 0

    divisors = []
    for i in range(1, a + 1):
        if a % i == 0:
            divisors.append(i)
    return divisors
# Post process
print("The divisors of the entered number are:", Divisor_Number(a))