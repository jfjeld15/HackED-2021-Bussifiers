## using numpy for generation of gradient image ##

# load and display image with matplotlib
from matplotlib import image
from matplotlib import pyplot
import matplotlib.pyplot as plt

# load numpy library
import numpy as np

f = np.array([1,2,3,6,11,31], dtype=float)
np.gradient(f)



"""
#load image as pixel array
im = image.imread('./images/rockylabels.png')

#display array as image
pyplot.imshow(im)
pyplot.show()
"""
