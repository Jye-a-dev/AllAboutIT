import ast

# Previous input
raw_input = input("Enter nested list representation (e.g. [1, 2], [3, 4]): ")
try:
    a = ast.literal_eval(raw_input) if raw_input.strip().startswith("[") else ast.literal_eval(f"[{raw_input}]")
except Exception:
    a = [x.strip() for x in raw_input.split(",") if x.strip()]

# Process
def flatten_Shallow_List(a):
    res = []
    for item in a:
        if isinstance(item, (list, tuple)):
            res.extend(item)
        else:
            res.append(item)
    return res

# Post process
print("Shallow flattened list:", flatten_Shallow_List(a))
