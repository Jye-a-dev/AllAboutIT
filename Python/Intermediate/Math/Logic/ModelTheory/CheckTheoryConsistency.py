import itertools

# Previous input
formula_set = [f.strip() for f in input("Enter formulas in theory (comma-separated): ").split(",") if f.strip()]
vars_list = [v.strip() for v in input("Enter variables (comma-separated): ").split(",") if v.strip()]

# Process
def is_Consistent_Formula_Set(formula_set, vars_list):
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
        if all(eval_expr(f, env) for f in formula_set):
            return True
    return False

# Post process
print("Theory is consistent:", is_Consistent_Formula_Set(formula_set, vars_list))
