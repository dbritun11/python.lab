import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(2, 0.5, 50)

x2 = np.random.normal(5, 0.5, 50)
y2 = np.random.normal(5, 0.5, 50)

x3 = np.random.normal(8, 0.5, 50)
y3 = np.random.normal(2, 0.5, 50)

plt.figure(figsize=(8, 6))

plt.scatter(x1, y1, color='red', label='Кластер 1', marker='o')
plt.scatter(x2, y2, color='blue', label='Кластер 2', marker='s')
plt.scatter(x3, y3, color='green', label='Кластер 3', marker='^')

plt.title('Точечная диаграмма с тремя кластерами', fontsize=16)
plt.xlabel('X значения', fontsize=12)
plt.ylabel('Y значения', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)

plt.savefig('scatter_clusters.png', dpi=300, bbox_inches='tight')
plt.show()
