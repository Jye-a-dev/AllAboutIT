# Previous input
a = input("Enter the URL: ")

# Process
from urllib.parse import urlparse

def is_Valid_Url(a):
    try:
        result = urlparse(a.strip())
        return all([result.scheme in ("http", "https", "ftp"), result.netloc])
    except Exception:
        return False

# Post process
print("Is valid URL:", is_Valid_Url(a))
