from dimacsConverter import dimacs_converter
from bruteForceSatSolver import brute_force_sat_solve
from dpllSatSolver import dpll_sat_solve

try:

    dimacs_filepath = input("Please enter the filepath to your dimacs file: ")

    clause_set, error_code = dimacs_converter(dimacs_filepath)

    if error_code == -1:

        quit()

    valid_choice = False

    while not valid_choice:

        print("Algorithm choices:")
        print("1. Brute Force Sat Solver")
        print("2. DPLL Sat Solver")

        algo_choice = int(input("Please choose your algorithm to evaluate this clause set: "))

        if algo_choice == 1:

            valid_choice = True
            brute_force_sat_solve(clause_set)

        elif algo_choice == 2:

            valid_choice = True
            print(dpll_sat_solve(clause_set, []))

        else:

            print("Invalid input. Please enter an appropriate choice")

except FileNotFoundError:

    print("Please ensure you have entered a valid filepath")


