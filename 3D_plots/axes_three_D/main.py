import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [1, 2, 3, 4]
Y = [2, 4, 6, 8]
Z = np.array([[1,2,3,4],[1,2,3,4]])


ax.plot_wireframe(X, Y, Z)
plt.show()