import itertools

def brute_force_sat_solve(clause_set):

    set_of_variables = set()

    # Establishes how many variables there are based on how many unique numbers we have
    # Note the negative of a number (variable) is not unique because it just represents the negation of that variable
    for clause in clause_set:

        for literal in clause:

            set_of_variables.add(abs(literal))

    num_of_variables = len(set_of_variables)

    # Possible Boolean Values
    boolean_values = [True, False]

    # All possible combinations of boolean values based on how many variables there are
    boolean_combinations = itertools.product(boolean_values, repeat=num_of_variables)

    for combination in boolean_combinations:

        # Counter for each boolean value in a particular combination
        i = 0

        # Dictionary that will store the variable-boolean value mapping of a particular combination
        bool_assignment_dict = dict()

        # List that contains the result of each clause
        clause_values = []

        for variable in set_of_variables:

            # Adds to the dictionary the var-bool mapping for each variable of a particular combination
            bool_assignment_dict[variable] = combination[i]

            # Increments i so the next boolean value in that combination is mapped to the next variable
            i += 1

        for clause in clause_set:

            clause_value = 0

            for literal in clause:

                # If the truth value of the literal is its dictionary mapping
                if literal > 0:

                    boolean_val_of_literal = bool_assignment_dict[literal]

                # If the truth value of the literal is the negation of its dictionary mapping
                else:

                    boolean_val_of_literal = not bool_assignment_dict[literal * -1]

                # Adds up the truth values of each literal
                # Truth = 1, False = 0
                clause_value += boolean_val_of_literal

            # If there is at least 1 literal that is true, that clause is true since each literal is connected by an OR
            if clause_value > 0:

                # Mark the clause as true in the list tracking the result of all clauses for that bool combination
                clause_values.append(1)

            # If all literals=false, the entire clause would be false
            else:

                # Mark the clause as false in the list tracking the result of all clauses for that bool combination
                clause_values.append(0)

        # If every clause in clause set returns true under this particular boolean combination
        if sum(clause_values) == len(clause_set):

            print(bool_assignment_dict)