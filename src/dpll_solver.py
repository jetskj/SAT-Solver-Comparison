def dpll(clauses, assignment=[]):
    if not clauses:
        return assignment  # All clauses satisfied => SAT
    if [] in clauses:
        return False       # Conflict => UNSAT

    # Unit propagation
    unit_clauses = [c[0] for c in clauses if len(c) == 1]
    while unit_clauses:
        literal = unit_clauses[0]
        assignment.append(literal)
        clauses = [
            [l for l in c if l != -literal]
            for c in clauses if literal not in c
        ]
        if not clauses:  # All clauses satisfied during unit propagation
            return assignment
        if [] in clauses:
            return False
        unit_clauses = [c[0] for c in clauses if len(c) == 1]

    if not clauses:
        return assignment  # Double check here too

    # Choose a variable
    variable = abs(clauses[0][0])
    for val in [variable, -variable]:
        new_assignment = assignment.copy()
        new_assignment.append(val)
        new_clauses = [
            [l for l in c if l != -val]
            for c in clauses if val not in c
        ]
        result = dpll(new_clauses, new_assignment)
        if result:
            return result
    return False
