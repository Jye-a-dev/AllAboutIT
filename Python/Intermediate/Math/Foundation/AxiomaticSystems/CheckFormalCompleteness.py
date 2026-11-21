import itertools

# Previous input
propositions = [p.strip() for p in input("Enter system propositions: ").split(",") if p.strip()]
all_atoms = [a.strip() for a in input("Enter all atomic formulas (comma-separated): ").split(",") if a.strip()]

# Process
def check_System_Completeness(propositions, all_atoms):
    # A system is syntactically complete if for every atom A, either Sigma |= A or Sigma |= not A
    def eval_expr(e, env):
        s = e.replace("<->", " == ").replace("<=>", " == ")
        s = s.replace("->", " <= ").replace("=>", " <= ")
        s = s.replace("xor", " ^ ").replace("~", " not ").replace("!", " not ")
        safe_dict = {k: bool(v) for k, v in env.items()}
        safe_dict["True"] = True
        safe_dict["False"] = False
        return bool(eval(s, {"__builtins__": None}, safe_dict))

    vars_list = sorted(list(set(all_atoms)))
    satisfying_models = []
    for combo in itertools.product([True, False], repeat=len(vars_list)):
        env = dict(zip(vars_list, combo))
        if all(eval_expr(p, env) for p in propositions):
            satisfying_models.append(env)

    if not satisfying_models:
        return False  # Inconsistent systems are not complete in standard semantics

    for atom in all_atoms:
        entails_atom = all(m.get(atom, False) is True for m in satisfying_models)
        entails_neg = all(m.get(atom, False) is False for m in satisfying_models)
        if not (entails_atom or entails_neg):
            return False
    return True

# Post process
print("Formal system is complete:", check_System_Completeness(propositions, all_atoms))
