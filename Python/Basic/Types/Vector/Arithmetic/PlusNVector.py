# Previous input
a = int(input("Enter the number of vectors to add: "))
# Process
def plus_vectors(a):
    v1 = [0, 0]
    for i in range(a):
        print("Vector", i + 1)
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        v1[0] += n1
        v1[1] += n2
    return v1

def add_N_Vectors(vectors):
    if isinstance(vectors, int):
        return plus_vectors(vectors)
    if not vectors:
        return []
    res = list(vectors[0])
    for v in vectors[1:]:
        for i in range(len(res)):
            res[i] += v[i]
    return res
# Post process
print("The sum of the vectors is:", plus_vectors(a))
