# ==========================================
# 1. PROPOSITIONAL LOGIC (Logic mệnh đề)
# ==========================================
from Python.Intermediate.Math.Logic.PropositionalLogic.LogicalImplies import logical_Implies
from Python.Intermediate.Math.Logic.PropositionalLogic.LogicalBiconditional import logical_Iff
from Python.Intermediate.Math.Logic.PropositionalLogic.LogicalXor import logical_Xor
from Python.Intermediate.Math.Logic.PropositionalLogic.LogicalNand import logical_Nand
from Python.Intermediate.Math.Logic.PropositionalLogic.LogicalNor import logical_Nor
from Python.Intermediate.Math.Logic.PropositionalLogic.EvaluateProposition import evaluate_Proposition
from Python.Intermediate.Math.Logic.PropositionalLogic.GenerateTruthTable import generate_Truth_Table
from Python.Intermediate.Math.Logic.PropositionalLogic.CheckTautology import is_Tautology
from Python.Intermediate.Math.Logic.PropositionalLogic.CheckContradiction import is_Contradiction
from Python.Intermediate.Math.Logic.PropositionalLogic.CheckContingency import is_Contingency
from Python.Intermediate.Math.Logic.PropositionalLogic.CheckLogicalEquivalence import are_Logically_Equivalent

# ==========================================
# 2. PREDICATE LOGIC (Logic vị từ)
# ==========================================
from Python.Intermediate.Math.Logic.PredicateLogic.UniversalQuantifier import for_All
from Python.Intermediate.Math.Logic.PredicateLogic.ExistentialQuantifier import exists_One
from Python.Intermediate.Math.Logic.PredicateLogic.UniqueExistential import exists_Unique
from Python.Intermediate.Math.Logic.PredicateLogic.NegateQuantifier import negate_Quantifier_Formula

# ==========================================
# 3. PROOF THEORY (Lý thuyết chứng minh)
# ==========================================
from Python.Intermediate.Math.Logic.ProofTheory.ModusPonens import apply_Modus_Ponens
from Python.Intermediate.Math.Logic.ProofTheory.ModusTollens import apply_Modus_Tollens
from Python.Intermediate.Math.Logic.ProofTheory.HypotheticalSyllogism import apply_Hypothetical_Syllogism
from Python.Intermediate.Math.Logic.ProofTheory.DisjunctiveSyllogism import apply_Disjunctive_Syllogism
from Python.Intermediate.Math.Logic.ProofTheory.ResolutionRule import resolve_Clauses
from Python.Intermediate.Math.Logic.ProofTheory.CheckSemanticEntailment import is_Valid_Entailment

# ==========================================
# 4. MODEL THEORY (Lý thuyết mô hình)
# ==========================================
from Python.Intermediate.Math.Logic.ModelTheory.FindSatisfyingModels import find_Satisfying_Models
from Python.Intermediate.Math.Logic.ModelTheory.CheckSatisfiability import is_Satisfiable
from Python.Intermediate.Math.Logic.ModelTheory.CheckTheoryConsistency import is_Consistent_Formula_Set

# ==========================================
# 5. COMPUTABILITY THEORY (Lý thuyết tính toán được)
# ==========================================
from Python.Intermediate.Math.Logic.ComputabilityTheory.PrimitiveRecursiveAdd import primitive_Recursive_Add
from Python.Intermediate.Math.Logic.ComputabilityTheory.PrimitiveRecursiveMult import primitive_Recursive_Mult
from Python.Intermediate.Math.Logic.ComputabilityTheory.AckermannFunction import ackermann_Function
from Python.Intermediate.Math.Logic.ComputabilityTheory.MuMinimization import mu_Minimization
from Python.Intermediate.Math.Logic.ComputabilityTheory.TuringMachineSimulator import simulate_Turing_Machine

# ==========================================
# EXPORTS
# ==========================================
__all__ = [
    name
    for name, value in globals().items()
    if not name.startswith("_") and callable(value)
]
