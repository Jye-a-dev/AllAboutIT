# Previous input
n = float(input("Enter number: "))
min_val = float(input("Enter min value: "))
max_val = float(input("Enter max value: "))

# Process
def clamp_Number(n, min_val, max_val):
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    return max(min_val, min(n, max_val))

# Post process
print("The clamped value is:", clamp_Number(n, min_val, max_val))
