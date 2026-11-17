# Previous input
a = input("Enter the string: ")

# Process
def run_Length_Encode(a):
    if not a:
        return ""
    result = []
    count = 1
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            count += 1
        else:
            result.append(f"{count}{a[i - 1]}")
            count = 1
    result.append(f"{count}{a[-1]}")
    return "".join(result)

# Post process
print("Run-length encoded string:", run_Length_Encode(a))
