# Previous input
a = input("Enter the string: ")

# Process
import base64

def to_Base64(a):
    return base64.b64encode(a.encode("utf-8")).decode("utf-8")

# Post process
print("Base64 encoded string:", to_Base64(a))
