import itertools

# Previous input
propositions = [p.strip() for p in input("Enter system propositions (comma-separated): ").split(",") if p.strip()]

# Process
def check_System_Consistency(propositions):
    if not propositions:
        return True
    # Extract variables
    vars_set = set()
    for p in propositions:
        tokens = p.replace("(", " ").replace(")", " ").replace("not", " ").replace("and", " ").replace("or", " ").replace("->", " ").replace("<->", " ").replace("~", " ").split()
        for tok in tokens:
            if tok not in ("True", "False", "xor", "<=>", "=>"):
                vars_set.add(tok)
    vars_list = sorted(list(vars_set))

    def eval_expr(e, env):
        s = e.replace("<->", " == ").replace("<=>", " == ")
        s = s.replace("->", " <= ").replace("=>", " <= ")
        s = s.replace("xor", " ^ ").replace("~", " not ").replace("!", " not ")
        safe_dict = {k: bool(v) for k, v in env.items()}
        safe_dict["True"] = True
        safe_dict["False"] = False
        return bool(eval(s, {"__builtins__": None}, safe_dict))

    for combo in itertools.product([True, False], repeat=len(vars_list)):
        env = dict(zip(vars_list, combo))
        if all(eval_expr(p, env) for p in propositions):
            return True
    return False

# Post process
print("Formal system is consistent:", check_System_Consistency(propositions))
