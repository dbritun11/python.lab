import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='z = sin(sqrt(x^2 + y^2))')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot: z = sin(sqrt(x^2 + y^2))')

plt.savefig('surface_plot.png', dpi=300, bbox_inches='tight')
plt.show()
