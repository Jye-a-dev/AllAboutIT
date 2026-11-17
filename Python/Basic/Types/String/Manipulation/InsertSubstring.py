# Previous input
a = input("Enter the string: ")
sub = input("Enter the substring to insert: ")
index = int(input("Enter the index: "))

# Process
def insert_Substring(a, sub, index):
    index = max(0, min(index, len(a)))
    return a[:index] + sub + a[index:]

# Post process
print("String after insertion:", insert_Substring(a, sub, index))
