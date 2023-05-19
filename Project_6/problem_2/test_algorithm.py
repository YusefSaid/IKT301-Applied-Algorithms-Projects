import reduction_algorithm
import generate_expressions
import time


def test_algorithm():
    number_of_tries = 100  # number of times we tests all the scenarios
    CONST = 1  # constant number of clauses or literals
    max_value = 1000  # max number of clauses or literals
    min_value = 2  # min number of clauses or literals
    step = 10  # difference in clauses or literals per datapoint

    number_of_literals = [i for i in range(min_value * CONST, (max_value - 1) * CONST, step * CONST)]

    increasing_clauses = [0 for i in range(int((max_value - 2) / step) + 1)]
    increasing_literals = [0 for i in range(int((max_value - 2) / step) + 1)]

    all_increasing_clauses = [[None for i in range(number_of_tries)] for j in range(int((max_value - 2) / step) + 1)]
    all_increasing_literals = [[None for i in range(number_of_tries)] for j in range(int((max_value - 2) / step) + 1)]

    for n in range(number_of_tries):
        print(n)
        for i in range(min_value, max_value, step):
            # one literal per clause, with increasing clauses
            CNF = generate_expressions.generate_CNF(i, CONST)
            time = test_scenario(CNF)
            increasing_clauses[int((i - 2) / step)] += time
            all_increasing_clauses[int((i - 2) / step)][n] = time

            # one clause with increasing literals in each clause
            CNF = generate_expressions.generate_CNF(CONST, i)
            time = test_scenario(CNF)
            increasing_literals[int((i - 2) / step)] += time
            all_increasing_literals[int((i - 2) / step)][n] = time

    # get the average time for each scenario
    for i in range(int((max_value - 2) / step) + 1):
        increasing_clauses[i] = increasing_clauses[i] / number_of_tries
        increasing_literals[i] = increasing_literals[i] / number_of_tries

    return {"increasing_clauses": increasing_clauses, "increasing_literals": increasing_literals}, \
           {"all_increasing_clauses": all_increasing_clauses, "all_increasing_literals": all_increasing_literals}, \
           number_of_literals


# retrieves the time it takes for our algorithm to reduce the CNF
def test_scenario(CNF):
    start = time.time()
    reduction_algorithm.reduce_to_clique_problem(CNF)
    end = time.time()
    return end - start
