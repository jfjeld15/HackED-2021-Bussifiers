## using numpy for generation of gradient image ##

# load libraries
import matplotlib.pyplot as plt
import numpy as np  # in windows terminal, run "pip install matplotlib"

# initialize grid
x_axis = np.linspace(-1, 1, 256)
y_axis = np.linspace(-1, 1, 256)

# generate np.array
xx, yy = np.meshgrid(x_axis, y_axis)
arr = np.sqrt(xx ** 2 + yy ** 2)

# toggle color
inner = np.array([0.1, 0.3, 0.4])[None, None, :]
outer = np.array([0.9, 1, 0.9])[None, None, :]

# control radius and radius color
arr = arr[:, :, None]
arr = (arr - 0.2) * outer + (1 - arr) * (inner)

plt.imshow(arr, cmap='gray')
plt.show()
