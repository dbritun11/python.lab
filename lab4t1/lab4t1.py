import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0.1, 1.2, 400)
b = 3.0

z1 = (np.sin(3*a)**(-2) + np.cos(7*a) - np.sin(6*a)) / (np.tan(a) + b - 2*a)
z2 = 13*(np.tan(a)**2) - 54*np.tan(a) + 98

z1 = np.where(np.abs(z1) > 100, np.nan, z1)
z2 = np.where(np.abs(z2) > 200, np.nan, z2)

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(a, z1, color='blue', label='z1', marker='o', markevery=30)
ax1.set_xlabel('a (угол альфа)', fontsize=12)
ax1.set_ylabel('z1', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_ylim(-50, 50)

ax2 = ax1.twinx()
ax2.plot(a, z2, color='red', linestyle='--', label='z2', marker='s', markevery=30)
ax2.set_ylabel('z2', color='red', fontsize=12)
ax2.tick_params(axis='y', labelcolor='red')
ax2.set_ylim(-200, 200)

plt.title('Графики функций z1 и z2', fontsize=16)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

ax1.annotate('Пример точки z1', xy=(0.8, z1[200]), xytext=(1.0, z1[200]+20),
             arrowprops=dict(facecolor='blue', shrink=0.05))
ax2.annotate('Пример точки z2', xy=(1.0, z2[250]), xytext=(1.1, z2[250]+50),
             arrowprops=dict(facecolor='red', shrink=0.05))

ax1.grid(True, linestyle='--', alpha=0.7)

plt.savefig('z1_z2_plot.png', dpi=300, bbox_inches='tight')
plt.show()
