import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Constants
NUM_PLANETS = 4  # Number of planets
ORBIT_RADIUSES = [4, 6, 8, 10]  # Simplified radii of orbits in arbitrary units
ORBIT_PERIODS = [80, 100, 150, 200]  # Simplified orbital periods in frames

# Initialize the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-12, 12])
ax.set_ylim([-12, 12])
ax.set_zlim([-12, 12])

# Representing the Sun with a large scatter plot point
ax.scatter([0], [0], [0], color="yellow", s=100)  # Sun at the center

# Initialize planets as empty points
planets = [ax.plot([], [], [], 'o', markersize=5)[0] for _ in range(NUM_PLANETS)]

# Animation update function
def update(frame):
    for i, planet in enumerate(planets):
        # Calculate the angle for the current frame
        angle = 2 * np.pi * (frame % ORBIT_PERIODS[i]) / ORBIT_PERIODS[i]

        # Update the position of the planet
        x = ORBIT_RADIUSES[i] * np.cos(angle)
        y = ORBIT_RADIUSES[i] * np.sin(angle)
        z = ORBIT_RADIUSES[i] * np.sin(angle) / 2  # Simple way to add 3D effect
        planet.set_data(x, y)
        planet.set_3d_properties(z)
    
    return planets

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, max(ORBIT_PERIODS), 500), interval=50, blit=False)

# Show the animation
plt.show()
