import itertools

# Previous input
expr = input("Enter propositional formula: ").strip()
vars_list = [v.strip() for v in input("Enter variables (comma-separated): ").split(",") if v.strip()]

# Process
def find_Satisfying_Models(expr, vars_list):
    def eval_expr(e, env):
        s = e.replace("<->", " == ").replace("<=>", " == ")
        s = s.replace("->", " <= ").replace("=>", " <= ")
        s = s.replace("xor", " ^ ").replace("~", " not ").replace("!", " not ")
        safe_dict = {k: bool(v) for k, v in env.items()}
        safe_dict["True"] = True
        safe_dict["False"] = False
        return bool(eval(s, {"__builtins__": None}, safe_dict))

    models = []
    for combo in itertools.product([True, False], repeat=len(vars_list)):
        env = dict(zip(vars_list, combo))
        if eval_expr(expr, env):
            models.append(env)
    return models

# Post process
print("Satisfying models:", find_Satisfying_Models(expr, vars_list))
