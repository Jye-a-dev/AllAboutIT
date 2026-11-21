import itertools

# Previous input
expr1 = input("Enter first proposition: ").strip()
expr2 = input("Enter second proposition: ").strip()
vars_list = [v.strip() for v in input("Enter variable names (comma-separated): ").split(",") if v.strip()]

# Process
def are_Logically_Equivalent(expr1, expr2, vars_list):
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
        if eval_expr(expr1, env) != eval_expr(expr2, env):
            return False
    return True

# Post process
print("Are logically equivalent:", are_Logically_Equivalent(expr1, expr2, vars_list))
