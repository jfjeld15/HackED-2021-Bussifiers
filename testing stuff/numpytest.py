## using numpy for generation of gradient image ##

# load libraries
import matplotlib.pyplot as plt
import numpy as np

##Just calculate 64*64
arr = np.zeros((64,64,3), dtype=np.uint8)
imgsize = arr.shape[:2]
innerColor = (0, 0, 0)
outerColor = (255, 255, 255)

x_axis = np.linspace(-1, 1, 256)
y_axis = np.linspace(-1, 1, 256)

xx, yy = np.meshgrid(x_axis, y_axis)
arr = np.sqrt(xx ** 2 + yy ** 2)

inner = np.array([0, 0, 0])[None, None, :]
outer = np.array([1, 1, 1])[None, None, :]

arr /= arr.max()
arr = arr[:, :, None]
arr = arr * outer + (1 - arr) * inner

plt.imshow(arr, cmap='gray')
plt.show()
