# Previous input

a = int(input("Enter the numbers of LCM: "))
# Process
def Lcm_Number(a):
    if a <= 0:
        return 0

    numbers = []
    for _ in range(a):
        n = int(input("Enter a number: "))
        numbers.append(n)

    if any(n == 0 for n in numbers):
        return 0

    lcm = abs(numbers[0])
    for n in numbers[1:]:
        n = abs(n)
        while n != 0:
            lcm, n = n, lcm % n
    return lcm

# Post process
print("The LCM of the entered numbers is:", Lcm_Number(a))