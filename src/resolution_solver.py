def resolve(clause1, clause2):
    for literal in clause1:
        if -literal in clause2:
            new_clause = list(set((clause1 + clause2)))
            new_clause.remove(literal)
            new_clause.remove(-literal)
            return new_clause
    return None

def resolution(clauses):
    new = set()
    clauses = [set(c) for c in clauses]
    while True:
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvent = resolve(list(clauses[i]), list(clauses[j]))
                if resolvent == []:
                    return True  # Unsatisfiable
                if resolvent:
                    new.add(frozenset(resolvent))
        if new.issubset(set(map(frozenset, clauses))):
            return False  # Satisfiable
        clauses.extend([set(c) for c in new])
