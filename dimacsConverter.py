def dimacs_converter(filepath):

    dimacs_file = open(filepath, "r")

    clause_set = [[]]

    # Clause counter - i.e. what clause we are currently at
    i = 0

    try:

        for each_line in dimacs_file:

            # Resets literal counter back to 0 at the start of a new line (clause)
            j = 0

            line = each_line.split()

            # If the line in the DIMACS file is a comment
            if line[0] == "c":

                continue

            # At the line that defines the problem
            elif line[0] == "p":

                num_of_variables = int(line[2])
                num_of_clauses = int(line[3])
                clause_set = [[0 for _ in range(num_of_variables)] for _ in range(num_of_clauses)]

            else:

                # Only iterates up to the 2nd last literal as the final one is always a 0 to signify the end of the literal
                for literal in line[:-1]:

                    clause_set[i][j] = int(literal)
                    j += 1

                i += 1

    except ValueError:
        print("Invalid File Format")
        return [[]], -1

    finally:
        dimacs_file.close()
        print("File closed")

    # List that will hold all clauses after being stripped of the 0s
    final_clause_set = []

    # Strips 0s from each clause
    for clause in clause_set:

        final_clause_set.append([literal for literal in clause if literal != 0])

    return final_clause_set, 0