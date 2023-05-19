def generate_CNF(number_of_clauses, literals_per_clause):
    CNF = []
    # generate a specified number of clauses and literals per clause.
    for i in range(number_of_clauses):
        clause = []
        for j in range(literals_per_clause):
            literal = j
            clause.append(literal)
        CNF.append(tuple(clause))
    return tuple(CNF)
