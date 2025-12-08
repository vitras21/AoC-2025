import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Required for 3D projection

# Define your 3D coordinates
point1 = (1, 2, 3)
point2 = (4, 5, 6)

# Create a figure and a 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(point1[0], point1[1], point1[2], color='red', label='Point 1')
ax.scatter(point2[0], point2[1], point2[2], color='blue', label='Point 2')

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Points Plot')
ax.legend()

plt.show()
