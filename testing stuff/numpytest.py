## using numpy for generation of gradient image ##

# load libraries
from matplotlib import image
from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=float)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

    return result

array = get_gradient_3d(512, 256, (0, 0, 0), (255, 255, 255), (True, True, True))
Image.fromarray(np.uint8(array)).save('./images/teehee.png', quality=95)



"""
#load image as pixel array
im = image.imread('./images/rockylabels.png')

#display array as image
pyplot.imshow(im)
pyplot.show()
"""
