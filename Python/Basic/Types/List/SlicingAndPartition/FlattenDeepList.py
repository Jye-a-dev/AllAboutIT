import ast

# Previous input
raw_input = input("Enter nested list representation (e.g. [1, [2, [3, 4]]]): ")
try:
    a = ast.literal_eval(raw_input) if raw_input.strip().startswith("[") else ast.literal_eval(f"[{raw_input}]")
except Exception:
    a = [x.strip() for x in raw_input.split(",") if x.strip()]

# Process
def flatten_Deep_List(a):
    res = []
    for item in a:
        if isinstance(item, (list, tuple)):
            res.extend(flatten_Deep_List(item))
        else:
            res.append(item)
    return res

# Post process
print("Deep flattened list:", flatten_Deep_List(a))
