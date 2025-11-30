import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(10, 10)

plt.figure(figsize=(8, 6))
plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Значение')

plt.title('Тепловая карта 10x10 случайных чисел', fontsize=16)

plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
plt.show()
