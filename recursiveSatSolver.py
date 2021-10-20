from uniqueVariables import unique_variables
from partialAssignmentSolver import solve_partial_assignment

# Function that determines the satisfiability of a clause set by recursively traversing a tree of possible assignments
def branching_sat_solve(clause_set, partial_assignment):

    # A set containing each unique variable in the clause set
    set_of_vars = unique_variables(clause_set)

    # Determines how many unique variables are in the clause set
    quantity_of_var = len(set_of_vars)

    # Checks for any empty clauses
    for clause in clause_set:

        if len(clause) == 0:

            return "UNSAT"

    # No clauses in the clause set (note this is different from an empty clause) -> clause set satisfiable
    if len(clause_set) == 0:

        return "SAT"

    # If the initial partial assignment is empty, run the following block
    if len(partial_assignment) == 0:

        # Recurse down the right branch -> variable 1 set to true
        first_var_true_branch = branching_sat_solve(clause_set, partial_assignment + [min(set_of_vars)])

        # Recurse down the left branch -> variable 1 set to false
        first_var_false_branch = branching_sat_solve(clause_set, partial_assignment + [-min(set_of_vars)])

    # If we have a valid number of partial assignments
    elif quantity_of_var >= len(partial_assignment):

        # Test the satisfiability of the clause set based on the partial assignment
        # If it is satisfiable, return the satisfying (partial) assignment
        if solve_partial_assignment(clause_set, partial_assignment):

            return partial_assignment

        # If this code runs it means we have not found a satisfying assignment although every variable has been assigned
        # That must suggest this particular assignment makes the clause set false
        elif quantity_of_var == len(partial_assignment):

            return False

        # If this code runs it means the partial assignment has not satisfied the clause set
        # However, we still have space to add another variable to the partial assignment list
        # That is what we will do in the following code
        else:

            next_var_to_add = 0

            # Go through all valid variables
            for variable in set_of_vars:

                # If the current variable is not already in the partial assignment list, we can add it
                if {variable, -variable}.isdisjoint(partial_assignment):

                    next_var_to_add = variable
                    break

            # Recurse into the branch where the next variable we add to the partial assignment list is set to True
            # Also recurse into the branch where the next variable we add to the partial assignment list is set to False
            # At the end of the recursion, a branch can have one of two values
            # Either it will contain a false value if that branch could not be satisfied
            # Or if that branch could be satisfied it will contain a satisfying partial assignment
            # If at least 1 branch is satisfied, that satisfying assignment will be stored at the top of the tree
            # I.e. either stored at first_var_true_branch or first_var_false_branch
            return branching_sat_solve(clause_set, partial_assignment + [next_var_to_add]) or branching_sat_solve(clause_set, partial_assignment + [-next_var_to_add])

    # If we have more variables in the partial assignment list than variables
    # This code should not run if the input is correct
    else:

        return False

    # If some point in this branch satisfied the clause set, return the satisfying assignment
    if first_var_true_branch:

        return first_var_true_branch

    # If some point in this branch satisfied the clause set, return the satisfying assignment
    elif first_var_false_branch:

        return first_var_false_branch

    # If neither branch (first var or first var false) satisfied the clause set, it must be unsatisfiable
    else:

        return "UNSAT"