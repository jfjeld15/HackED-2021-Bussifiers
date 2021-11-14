## using numpy for generation of gradient image ##

# load and display image with matplotlib
from matplotlib import image
from matplotlib import pyplot

# load numpy library
import numpy as np

#load image as pixel array
im = image.imread('./images/rockylabels.png')

#display array as image
pyplot.imshow(im)
pyplot.show()

