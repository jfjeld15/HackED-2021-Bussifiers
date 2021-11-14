## using numpy for generation of gradient image ##

# load libraries
import matplotlib.pyplot as plt
import numpy as np  # in windows terminal, run "pip install matplotlib"

# initialize grid
x_axis = np.linspace(-1, 1, 833)
y_axis = np.linspace(-1, 1, 766)

# center of Whistler
center_whis = [(1 - 2/833*105), (1 - 2/766*498)]
center_sP = [(1 - 2/833*362), (1 - 2/766*404)]

# generate np.array
xx_whis, yy_whis = np.meshgrid(x_axis+center_whis[0], y_axis+center_whis[1])
xx_sP, yy_sP = np.meshgrid(x_axis+center_sP[0], y_axis+center_sP[1])
arr = np.sqrt(xx_whis ** 2 + yy_whis ** 2)

# adj color
inner = np.array([0.1, 0.3, 0.3])[None, None, :]
outer = np.array([0.8, 0.9, 0.8])[None, None, :]

# adj radius size
arr = arr[:, :, None]
arr = (arr+0.8) * outer + (arr) * (inner+0.4)

# disp gradient 
plt.figure(figsize = (8.33, 7.66))
plt.imshow(arr[:], cmap='gray')
plt.savefig('./images/grad_plt.png')
plt.show()

