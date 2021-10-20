def unit_propagate(clause_set):

    unit_prop_complete = True

    initial_num_of_unit_clauses = 0

    all_unit_clause_literals = []

    # For loop to check initial number of unit clauses
    for clause in clause_set:

        if len(clause) == 1:

            initial_num_of_unit_clauses += 1
            break

    # If the clause set can be simplified with unit propagation
    if initial_num_of_unit_clauses > 0:

        unit_prop_complete = False

    # As long as unit clauses exist
    while not unit_prop_complete:

        # List that will hold the literal that is in the unit clause
        current_unit_clause_literals = []

        # List that will hold the updated clause set after one round of unit propagation
        simplified_clause_set = []

        # Adds all the literals that form each unit clause
        for clause in clause_set:

            if len(clause) == 1:

                current_unit_clause_literals.append(clause[0])
                all_unit_clause_literals.append(clause[0])
                break

        # List that will hold the negation of the literals that form each unit clause
        negation_of_current_unit_clause_literals = [-x for x in current_unit_clause_literals]

        # If the negation of a unit clause literal exists in a clause, delete that literal from the clause
        for clause in clause_set:

            for neg_literal in negation_of_current_unit_clause_literals:

                if neg_literal in clause:

                    clause.remove(neg_literal)

        # If a clause contains a unit clause literal, delete that entire clause
        for clause in clause_set:

            if set(clause).isdisjoint(current_unit_clause_literals):

                simplified_clause_set.append(clause)

        # Variable to contain the number of unit clauses that now exist after 1 round of unit propagation
        remaining_unit_clauses = 0

        # Establishes how many unit clauses now exist after 1 round of unit propagation
        for clause in simplified_clause_set:

            if len(clause) == 1:

                remaining_unit_clauses += 1

            else:

                continue

        # If there are no longer any unit clauses, then unit propagation must be complete
        # If not, we re-apply unit propagation on the simplified clause set
        if remaining_unit_clauses == 0:

            unit_prop_complete = True

        clause_set = simplified_clause_set

    return clause_set, all_unit_clause_literals


def pure_literal_eliminate(clause_set):

    # Initially assume pure literals exist in the clause set
    process_complete = False

    all_pure_literals = []

    # As long as pure literals exist in the updated clause set
    while not process_complete:

        # Initialise empty set to hold all literal assignments
        literal_assignments = set()

        # List that will hold all pure literals of the latest clause set
        pure_literals = []

        # List that will hold the updated clause set after 1 round of pure literal elimination
        simplified_clause_set = []

        # For loop to determine unique literal assignments within the clause set
        for clause in clause_set:

            for literal in clause:

                literal_assignments.add(literal)

        # For loop to add pure literals to the pure literals list
        for literal_assignment in literal_assignments:

            if -literal_assignment not in literal_assignments:

                pure_literals.append(literal_assignment)
                all_pure_literals.append(literal_assignment)

        # If there are no pure literals, break out of the while loop
        if len(pure_literals) == 0:

            break

        # For loop that only adds clauses not containing pure literals to the simplified clause set
        # I.e. deletes clauses that contain pure literals from the clause set
        for clause in clause_set:

            if set(clause).isdisjoint(pure_literals):

                simplified_clause_set.append(clause)

        # Updates the clause set so that pure literal elimination can be run again (if necessary)
        clause_set = simplified_clause_set

    # Returns the updated clause set after pure literal elimination can no longer be applied
    return clause_set, all_pure_literals