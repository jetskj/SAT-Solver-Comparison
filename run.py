import matplotlib.pyplot as plt
import numpy as np

# Data
instances = ['uf75-325', 'aim-100', 'hanoi4']
solvers = ['Resolution', 'DP', 'DPLL']
runtime = {
    'Resolution': [12.54, 300, 58.6],
    'DP': [1.82, 3.74, 2.21],
    'DPLL': [0.47, 1.15, 0.92]
}

# Plot
x = np.arange(len(instances))
width = 0.25

fig, ax = plt.subplots()
for i, solver in enumerate(solvers):
    ax.bar(x + i * width, runtime[solver], width, label=solver)

ax.set_ylabel('Runtime (s)')
ax.set_title('Runtime Comparison by Instance and Solver')
ax.set_xticks(x + width)
ax.set_xticklabels(instances)
ax.legend()
plt.tight_layout()

# Save the figure
plt.savefig('figures/runtime_comparison.png')
plt.show()
