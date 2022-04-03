from skimage import io
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

co = io.imread('sample_Images/blocks.tif')
cf = np.float32(co)
a = fig.add_subplot(231)
a.title.set_text('original')
io.imshow(np.uint8(cf))

cp = np.ubyte(np.clip((cf+128), 0, 255))
a = fig.add_subplot(232)
a.title.set_text('+128')
io.imshow(cp)


cp = np.ubyte(np.clip((cf-128), 0, 255))
a = fig.add_subplot(233)
a.title.set_text('-128')
io.imshow(cp)

cp = np.ubyte(np.clip((cf*0.5), 0, 255))
a = fig.add_subplot(234)
a.title.set_text('x*0.5')
io.imshow(np.uint8(cp))

cp = np.ubyte(np.clip((cf*2), 0, 255))
a = fig.add_subplot(235)
a.title.set_text('x*2')
io.imshow(cp)


cp = np.ubyte(np.clip((cf*0.5+128), 0, 255))
a = fig.add_subplot(236)
a.title.set_text('x*0.5+128')
io.imshow(cp)

io.show()
