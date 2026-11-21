# Previous input
quantifier = input("Enter quantifier ('forall' or 'exists'): ").strip()
predicate_str = input("Enter predicate formula string P(x): ").strip()

# Process
def negate_Quantifier_Formula(quantifier, predicate_str):
    q = quantifier.strip().lower()
    if q in ("forall", "\\forall", "all"):
        return ("exists", f"not ({predicate_str})")
    elif q in ("exists", "\\exists", "some"):
        return ("forall", f"not ({predicate_str})")
    raise ValueError(f"Unknown quantifier: {quantifier}")

# Post process
print("Negated quantified formula:", negate_Quantifier_Formula(quantifier, predicate_str))
