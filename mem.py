import matplotlib.pyplot as plt
import numpy as np

# Data
instances = ['uf75-325', 'aim-100', 'hanoi4']
solvers = ['Resolution', 'DP', 'DPLL']
memory = {
    'Resolution': [88.1, 300, 120.4],
    'DP': [14.6, 23.1, 18.3],
    'DPLL': [10.2, 12.9, 11.5]
}

# Plot
x = np.arange(len(instances))
width = 0.25

fig, ax = plt.subplots()
for i, solver in enumerate(solvers):
    ax.bar(x + i * width, memory[solver], width, label=solver)

ax.set_ylabel('Memory Usage (MB)')
ax.set_title('Memory Usage Comparison by Instance and Solver')
ax.set_xticks(x + width)
ax.set_xticklabels(instances)
ax.legend()
plt.tight_layout()

# Save the figure
plt.savefig('figures/memory_comparison.png')
plt.show()