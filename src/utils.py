def load_cnf(file_path):
    clauses = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(('p', 'c', '%', '0')):
                continue
            clause = list(map(int, line.split()))
            if clause[-1] == 0:
                clause.pop()  # remove trailing 0
            clauses.append(clause)
    return clauses
