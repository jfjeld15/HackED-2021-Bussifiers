## using numpy for generation of gradient image ##

# load libraries
import matplotlib.pyplot as plt
import numpy as np  # in windows terminal, run "pip install matplotlib"

# initialize grid
x_axis = np.linspace(-1, 1, 833)
y_axis = np.linspace(-1, 1, 766)

# generate np.array
xx, yy = np.meshgrid(x_axis, y_axis)
arr = np.sqrt(xx ** 2 + yy ** 2)

# adj color
inner = np.array([0.1, 0.3, 0.3])[None, None, :]
outer = np.array([0.8, 0.9, 0.8])[None, None, :]

# adj radius size
arr = arr[:, :, None]
arr = (arr+0.8) * outer + (arr) * (inner+0.4)

# disp gradient 
plt.imshow(arr[:], cmap='gray')
plt.savefig('./images/grad_plt.png', transparent = True)
plt.show()

