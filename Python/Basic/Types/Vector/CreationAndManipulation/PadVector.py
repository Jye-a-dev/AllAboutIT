# Previous input
v = [float(x) for x in input("Enter vector (comma-separated): ").split(",")]
target_len = int(input("Enter target length: "))
pad_value = float(input("Enter pad value: "))

# Process
def pad_Vector(v, target_len, pad_value=0.0):
    if len(v) >= target_len:
        return list(v)
    return list(v) + [pad_value] * (target_len - len(v))

# Post process
print("Padded vector:", pad_Vector(v, target_len, pad_value))
