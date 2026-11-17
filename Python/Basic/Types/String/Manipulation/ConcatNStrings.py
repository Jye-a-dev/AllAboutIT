# Previous input
strings = input("Enter strings separated by comma: ").split(",")

# Process
def concat_N_Strings(strings):
    return "".join(strings)

# Post process
print("Concatenated string:", concat_N_Strings(strings))
