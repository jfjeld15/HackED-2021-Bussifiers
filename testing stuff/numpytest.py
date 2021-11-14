## using numpy for generation of gradient image ##

# load and display image with matplotlib
from matplotlib import image
from matplotlib import pyplot

# load numpy library
import numpy as np

def generate_block():
    x = np.ones((50, 50, 3))
    x[:, :, 0:3] = np.random.uniform(0, 1, (3,))
    plt.imshow(x)
    plt.figure() 

    y = np.ones((50, 50, 3))
    y[:,:,0:3] = np.random.uniform(0, 1, (3,))
    plt.imshow(y)

    plt.figure()
    c = np.linspace(0, 1, 50)[:, None, None]
    gradient = x + (y - x) * c
    plt.imshow(gradient)
    return x, y, gradient



"""
#load image as pixel array
im = image.imread('./images/rockylabels.png')

#display array as image
pyplot.imshow(im)
pyplot.show()
"""
