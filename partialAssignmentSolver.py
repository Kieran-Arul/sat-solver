# Function that determines the satisfiability of a clause set based on a partial assignment
def solve_partial_assignment(clause_set, partial_assignment):

    # List that will contain 1s or 0s depending on what each clause evaluates to
    clause_values = []

    # Dictionary that will contain each variable to boolean mapping
    bool_assignment_dict = dict()

    # Loop through partial assignment list
    for literal_assignment in partial_assignment:

        # If the number > 0, means we need to set that variable to true
        if literal_assignment > 0:

            # Create mapping whereby that variable is set to true
            bool_assignment_dict[abs(literal_assignment)] = True

        # If the number < 0, means we need to set that variable to false
        else:

            # Create mapping whereby that variable is set to false
            bool_assignment_dict[abs(literal_assignment)] = False

    # Loop over each clause in the clause set
    for clause in clause_set:

        # Variable that will be more than 0 if the clause is true, and 0 if the clause is false
        clause_value = 0

        # Loop over each literal in the current clause
        for literal in clause:

            # If we have already assigned that literal a boolean value in the partial assignment:
            if abs(literal) in bool_assignment_dict:

                # If that literal's boolean value is what it was assigned in the partial assignment
                if literal > 0:

                    # Assign that boolean value to that literal
                    bool_val_of_literal = bool_assignment_dict[abs(literal)]

                # If that literal's boolean value is the negation of what it was assigned in the partial assignment
                else:

                    # Assign the negation of the partial assignment boolean value to that literal
                    bool_val_of_literal = not bool_assignment_dict[abs(literal)]

                # Add the boolean value of the literal to the clause value
                # True = 1
                # False = 0
                clause_value += bool_val_of_literal

            # If the particular literal has not been assigned a boolean in the partial assignment
            else:

                # Assume that literal was set to false
                clause_value += 0

        # At least 1 literal in the clause set were true -> clause evaluates to true
        if clause_value > 0:

            clause_values.append(1)

        # None of the literals in the clause set were true -> clause evaluates to false
        else:

            clause_values.append(0)

    # Every clause evaluated to true -> clause set is true
    if sum(clause_values) == len(clause_set):

        return True

    # At least one clause evaluated to false -> clause set is false
    else:

        return False