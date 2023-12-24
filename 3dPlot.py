import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Function to generate sample data
def generate_sample_data():
    np.random.seed(0)  # For reproducible results
    x = np.random.standard_normal(100)
    y = np.random.standard_normal(100)
    z = np.random.standard_normal(100)
    return x, y, z

# Function to create a 3D scatter plot
def plot_3d_scatter(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot
    scatter = ax.scatter(x, y, z)

    # Adding labels and title
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Scatter Plot')

    # Show plot
    plt.show()

# Main function to orchestrate the plotting
def main():
    x, y, z = generate_sample_data()
    plot_3d_scatter(x, y, z)

if __name__ == "__main__":
    main()
