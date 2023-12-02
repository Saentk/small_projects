import plotly.graph_objs as go
import numpy as np

# Set a seed for reproducibility
np.random.seed(0)

# Generate 100 random data points for each axis
# np.random.rand() generates random numbers between 0 and 1
x = np.random.rand(100)  # X-axis data
y = np.random.rand(100)  # Y-axis data
z = np.random.rand(100)  # Z-axis data

# Creating a 3D scatter plot using Plotly
trace = go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',  # 'markers' means we are plotting dots, not lines
    marker=dict(
        size=10,  # Size of each marker (dot)
        color=z,  # Assign a color to each marker based on its z-value
        colorscale='Viridis',  # Colorscale to be used for marker colors
        opacity=0.8  # Transparency of the markers
    )
)

# Wrapping the trace in a list to conform to Plotly's data structure
data = [trace]

# Defining layout of the plot
layout = go.Layout(
    margin=dict(l=0, r=0, b=0, t=0),  # Reducing margins around the plot
    title='Interactive 3D Scatter Plot'  # Title of the plot
)

# Creating a figure object that combines the data and layout
fig = go.Figure(data=data, layout=layout)

# To display the plot in a Jupyter notebook, uncomment the next line:
# fig.show()

# To display the plot as a standalone program, use the following:
if __name__ == "__main__":
    import plotly.io as pio
    pio.renderers.default = 'browser'  # Set the default renderer to browser
    fig.show()  # Show the figure in the browser
