import skimage.util as ut
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

co = io.imread('sample_Images/twins.tif')
inverted_img = ut.invert(co)
a = fig.add_subplot(131)
a.title.set_text('original')

io.imshow(co)
a = fig.add_subplot(132)
a.title.set_text('complement<128')
ico = np.maximum(co, inverted_img) # complement<128
io.imshow(ico)

ico = np.minimum(co, inverted_img) # complement>128
a = fig.add_subplot(133)
a.title.set_text('complement>128')
io.imshow(ico)

io.show()
