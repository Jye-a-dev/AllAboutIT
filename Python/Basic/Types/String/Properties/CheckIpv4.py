# Previous input
a = input("Enter the IPv4 address: ")

# Process
import ipaddress

def is_Valid_Ipv4(a):
    try:
        ipaddress.IPv4Address(a.strip())
        return True
    except ValueError:
        return False

# Post process
print("Is valid IPv4 address:", is_Valid_Ipv4(a))
