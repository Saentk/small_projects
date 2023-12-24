import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to create sample data
def create_sample_data():
    # Creating a DataFrame with random data
    np.random.seed(0)
    data = pd.DataFrame({
        'x': np.random.rand(100),
        'y': np.random.rand(100),
        'group': np.random.choice(['A', 'B', 'C'], 100),
        'size': np.random.rand(100) * 100
    })
    return data

# Function to plot interactive scatter plot
def plot_interactive_scatter(data):
    # Grouping data for color coding
    groups = data.groupby('group')

    # Creating the scatter plot
    fig, ax = plt.subplots()
    for name, group in groups:
        ax.scatter(group['x'], group['y'], marker='o', s=group['size'], label=name)

    # Customizing the plot
    ax.set_xlabel('X Axis Label')
    ax.set_ylabel('Y Axis Label')
    ax.set_title('Interactive Scatter Plot')
    ax.legend()

    # Show the plot with interactive features
    plt.show()

# Main function to orchestrate data creation and plotting
def main():
    data = create_sample_data()  # Replace with real data loading if needed
    plot_interactive_scatter(data)

if __name__ == "__main__":
    main()
