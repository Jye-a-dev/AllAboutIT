# Previous input
sequence = [int(x.strip()) for x in input("Enter sequence of non-negative integers (comma-separated): ").split(",") if x.strip()]

# Process
def godel_Encode_Sequence(sequence):
    def get_primes(count):
        primes = []
        candidate = 2
        while len(primes) < count:
            is_p = True
            for p in primes:
                if p * p > candidate:
                    break
                if candidate % p == 0:
                    is_p = False
                    break
            if is_p:
                primes.append(candidate)
            candidate += 1
        return primes

    if not sequence:
        return 1
    primes = get_primes(len(sequence))
    res = 1
    for p, exp in zip(primes, sequence):
        res *= (p ** exp)
    return res

# Post process
print("Gödel encoded number:", godel_Encode_Sequence(sequence))
