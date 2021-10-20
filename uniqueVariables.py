# Function that helps determine the number of variables in a clause set
def unique_variables(clause_set):

    set_of_variables = set()

    for clause in clause_set:

        for literal in clause:

            set_of_variables.add(abs(literal))

    return set_of_variables