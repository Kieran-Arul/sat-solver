from optimisations import unit_propagate, pure_literal_eliminate
from recursiveSatSolver import branching_sat_solve

def dpll_sat_solve(clause_set, partial_assignment):

    # Apply unit propagation to the clause set
    clause_set, unit_clause_literals = unit_propagate(clause_set)

    # Apply pure literal elimination to the clause set
    clause_set, pure_literals = pure_literal_eliminate(clause_set)

    # If these simplification processes have deleted all clauses, the clause set must be satisfiable
    if len(clause_set) == 0:

        return unit_clause_literals + pure_literals

    # If some clauses still exist after simplification
    else:

        result = branching_sat_solve(clause_set, partial_assignment)

        # If the clause set is satisfiable, meaning we can get a possibly incomplete partial assignment list back
        # We need to include the pure literals that were eliminated in pure literal elimination
        if isinstance(result, list):

            result = result + unit_clause_literals + pure_literals

        return result