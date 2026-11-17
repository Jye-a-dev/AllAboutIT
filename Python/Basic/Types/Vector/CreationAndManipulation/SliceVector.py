# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
step = int(input("Enter step: "))

# Process
def slice_Vector(v, start, end, step=1):
    return v[start:end:step]

# Post process
print("Sliced vector:", slice_Vector(v, start, end, step))
