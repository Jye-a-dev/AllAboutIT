import itertools

# Previous input
premises = [p.strip() for p in input("Enter premises (comma-separated): ").split(",") if p.strip()]
conclusion = input("Enter conclusion: ").strip()
vars_list = [v.strip() for v in input("Enter variable names (comma-separated): ").split(",") if v.strip()]

# Process
def is_Valid_Entailment(premises, conclusion, vars_list):
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
        if all(eval_expr(p, env) for p in premises):
            if not eval_expr(conclusion, env):
                return False
    return True

# Post process
print("Semantic entailment holds:", is_Valid_Entailment(premises, conclusion, vars_list))
