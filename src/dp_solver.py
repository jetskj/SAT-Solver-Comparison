def resolve(clause1, clause2):
    for literal in clause1:
        if -literal in clause2:
            new_clause = list(set(clause1 + clause2))
            new_clause.remove(literal)
            new_clause.remove(-literal)
            return new_clause
    return None

def dp(clauses):
    if not clauses:
        return True
    if [] in clauses:
        return False

    # Pick a variable (naive first literal)
    variable = abs(clauses[0][0])
    pos = [c for c in clauses if variable in c]
    neg = [c for c in clauses if -variable in c]
    rest = [c for c in clauses if variable not in c and -variable not in c]

    resolvents = []
    for p in pos:
        for n in neg:
            r = resolve(p, n)
            if r is not None:
                resolvents.append(r)

    return dp(rest + resolvents)
