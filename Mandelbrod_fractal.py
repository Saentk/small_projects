import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

def plot_fractal(xmin, xmax, ymin, ymax, width=1000, height=1000, max_iter=256):
    dpi = 80
    img_width = width / dpi
    img_height = height / dpi
    fig, ax = plt.subplots(figsize=(img_width, img_height), dpi=dpi)
    r1, r2, n3 = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    ax.imshow(n3.T, extent=[xmin, xmax, ymin, ymax], cmap="hot")
    plt.show()

if __name__ == '__main__':
    plot_fractal(-2.0, 0.5, -1.25, 1.25)
