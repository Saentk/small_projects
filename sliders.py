import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# Initial parameters
init_amplitude = 1.0
init_frequency = 1.0

# Create the figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)

# Time array
t = np.arange(0.0, 1.0, 0.001)

# Sine wave function
def sine_wave(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)

# Initial plot
s = sine_wave(t, init_amplitude, init_frequency)
l, = plt.plot(t, s, lw=2)

# Adjusting plot limits
ax.set_xlim([0, 1])
ax.set_ylim([-2, 2])

# Slider axes
axcolor = 'lightgoldenrodyellow'
ax_amp = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_freq = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=axcolor)

# Sliders
s_amp = Slider(ax_amp, 'Amplitude', 0.1, 2.0, valinit=init_amplitude)
s_freq = Slider(ax_freq, 'Frequency', 0.1, 3.0, valinit=init_frequency)

# Update function
def update(val):
    amp = s_amp.val
    freq = s_freq.val
    l.set_ydata(sine_wave(t, amp, freq))
    fig.canvas.draw_idle()

# Register the update function with each slider
s_amp.on_changed(update)
s_freq.on_changed(update)

plt.show()
