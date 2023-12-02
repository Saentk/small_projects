import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constants
NUM_STARS = 150  # Number of stars
MAX_RADIUS = 5  # Maximum radius of star orbits
SPIRAL_TURNS = 3  # Number of spiral turns

# Initialize figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-MAX_RADIUS, MAX_RADIUS)
ax.set_ylim(-MAX_RADIUS, MAX_RADIUS)
ax.set_facecolor('black')  # Set background to black

# Central massive object (like a black hole)
central_mass = plt.Circle((0, 0), 0.3, color='white')
ax.add_artist(central_mass)

# Initialize stars with random positions
np.random.seed(0)  # For reproducibility
initial_radii = np.random.rand(NUM_STARS) * MAX_RADIUS
initial_angles = np.random.rand(NUM_STARS) * 2 * np.pi
stars = [ax.plot(radius * np.cos(angle), radius * np.sin(angle), 'o', markersize=np.random.rand() * 2 + 1,
                 color=np.random.choice(['white', 'yellow', 'blue', 'red']))[0]
         for radius, angle in zip(initial_radii, initial_angles)]

# Animation update function
def update(frame):
    for i, star in enumerate(stars):
        # Decrease the radius to simulate spiraling inwards
        radius = initial_radii[i] * (1 - frame / 500)
        angle = initial_angles[i] + 2 * np.pi * SPIRAL_TURNS * frame / 500

        # Update the position of the star
        x, y = radius * np.cos(angle), radius * np.sin(angle)
        star.set_data(x, y)
    
    return stars

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 500, 1000), interval=20, blit=True)

# Show the animation
plt.show()
