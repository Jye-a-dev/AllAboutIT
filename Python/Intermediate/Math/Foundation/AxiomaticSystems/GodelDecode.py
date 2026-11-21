# Previous input
number = int(input("Enter Gödel number: "))

# Process
def godel_Decode_Number(number):
    if number <= 1:
        return []
    primes = []
    candidate = 2
    exponents = []
    temp = number
    while temp > 1:
        # Check if candidate is prime
        is_p = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_p = False
                break
        if is_p:
            primes.append(candidate)
            exp = 0
            while temp % candidate == 0:
                exp += 1
                temp //= candidate
            exponents.append(exp)
        candidate += 1
    # Trim trailing zeroes if any
    while exponents and exponents[-1] == 0:
        exponents.pop()
    return exponents

# Post process
print("Gödel decoded sequence:", godel_Decode_Number(number))
