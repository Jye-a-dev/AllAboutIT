# Previous input
expr = input("Enter propositional expression (e.g. 'p and (q or not p)'): ").strip()
env_input = input("Enter variable assignments (e.g. 'p:True, q:False'): ").strip()
env = {}
if env_input:
    for pair in env_input.split(","):
        if ":" in pair:
            k, v = pair.split(":", 1)
            env[k.strip()] = v.strip().lower() in ("true", "1", "t")

# Process
def evaluate_Proposition(expr, env):
    # Normalize logic operators into Python safe boolean operators
    s = expr
    s = s.replace("<->", " == ").replace("<=>", " == ")
    s = s.replace("->", " <= ").replace("=>", " <= ")
    s = s.replace("xor", " ^ ")
    s = s.replace("~", " not ").replace("!", " not ")
    safe_dict = {k: bool(v) for k, v in env.items()}
    safe_dict["True"] = True
    safe_dict["False"] = False
    return bool(eval(s, {"__builtins__": None}, safe_dict))

# Post process
print("Evaluation result:", evaluate_Proposition(expr, env))
