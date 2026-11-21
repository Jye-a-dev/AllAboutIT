import math

# Previous input
limit = int(input("Enter upper bound for hypotenuse c: "))

# Process
def generate_Pythagorean_Triples(limit):
    triples = []
    if limit < 5:
        return triples
    for a in range(1, limit):
        for b in range(a, limit):
            c_sq = a * a + b * b
            c = math.isqrt(c_sq)
            if c > limit:
                break
            if c * c == c_sq:
                triples.append((a, b, c))
    return triples

# Post process
print("Pythagorean triples:", generate_Pythagorean_Triples(limit))
