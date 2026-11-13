# Previous input
a = int(input("Enter the numbers of GCD: "))
# Process
def Gcd_Number(a):
    if a <= 0:
        return 0

    numbers = []
    for _ in range(a):
        n = int(input("Enter a number: "))
        numbers.append(n)

    gcd = abs(numbers[0])
    for n in numbers[1:]:
        n = abs(n)
        while n != 0:
            gcd, n = n, gcd % n
    return gcd

# Post process
print("The GCD of the entered numbers is:", Gcd_Number(a))