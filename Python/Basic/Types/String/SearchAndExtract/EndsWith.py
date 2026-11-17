# Previous input
a = input("Enter the string: ")
suffix = input("Enter the suffix: ")

# Process
def ends_With(a, suffix):
    return a.endswith(suffix)

# Post process
print("Ends with suffix:", ends_With(a, suffix))
