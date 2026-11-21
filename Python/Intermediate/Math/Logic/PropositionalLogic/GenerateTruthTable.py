import itertools

# Previous input
expr = input("Enter propositional expression: ").strip()
vars_list = [v.strip() for v in input("Enter variable names (comma-separated): ").split(",") if v.strip()]

# Process
def generate_Truth_Table(expr, vars_list):
    def eval_expr(e, env):
        s = e.replace("<->", " == ").replace("<=>", " == ")
        s = s.replace("->", " <= ").replace("=>", " <= ")
        s = s.replace("xor", " ^ ").replace("~", " not ").replace("!", " not ")
        safe_dict = {k: bool(v) for k, v in env.items()}
        safe_dict["True"] = True
        safe_dict["False"] = False
        return bool(eval(s, {"__builtins__": None}, safe_dict))

    table = []
    for combo in itertools.product([True, False], repeat=len(vars_list)):
        env = dict(zip(vars_list, combo))
        val = eval_expr(expr, env)
        row = dict(env)
        row["result"] = val
        table.append(row)
    return table

# Post process
print("Truth table rows:", generate_Truth_Table(expr, vars_list))
