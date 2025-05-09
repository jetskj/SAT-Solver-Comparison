import time
import psutil
from dpll_solver import dpll
from dp_solver import dp
from resolution_solver import resolution
from utils import load_cnf

def run_experiment(solver, clauses):
    start = time.time()
    process = psutil.Process()
    mem_before = process.memory_info().rss
    result = solver([clause.copy() for clause in clauses])  # isolate input
    mem_after = process.memory_info().rss
    return {
        'result': result,
        'time': time.time() - start,
        'memory': (mem_after - mem_before) / 1024  # in KB
    }

if __name__ == "__main__":
    clauses = load_cnf("../data/sample.cnf")

    for name, solver in {
        "Resolution": resolution,
        "DP": dp,
        "DPLL": dpll,
    }.items():
        print(f"Running {name}...")
        stats = run_experiment(solver, clauses)
        print(f"{name} → SAT? {stats['result']}, Time: {stats['time']:.4f}s, Memory: {stats['memory']:.2f} KB")
