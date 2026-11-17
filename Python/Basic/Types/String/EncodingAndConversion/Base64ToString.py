# Previous input
a = input("Enter base64 string: ")

# Process
import base64

def from_Base64(a):
    try:
        return base64.b64decode(a.encode("utf-8")).decode("utf-8", errors="replace")
    except Exception:
        return ""

# Post process
print("Decoded string from base64:", from_Base64(a))
