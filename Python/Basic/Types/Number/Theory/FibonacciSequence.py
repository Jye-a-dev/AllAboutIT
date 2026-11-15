# Previous input
n = int(input("Enter number of Fibonacci terms: "))

# Process
def Fibonacci_Sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

# Post process
print("The Fibonacci sequence is:", Fibonacci_Sequence(n))
