import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(2, 3, 1)
ax.title.set_text('uint8')
co = io.imread('sample_Images/caribou.tif')
io.imshow(co)

ax.title.set_text('uint8')
print(co.dtype, co.min(), co.max())

ax1 = fig.add_subplot(2, 3, 2)
ax1.title.set_text('np.float64')
cf = np.float64(co)
io.imshow(cf)

ax2 = fig.add_subplot(2, 3, 3)
ax2.title.set_text('np.int64')
ci = np.int64(co)
io.imshow(ci)

ax3 = fig.add_subplot(2, 3, 4)
ax3.title.set_text('np.float64(co)/256')
cs = np.float64(co) / 256
io.imshow(cs)

ax4 = fig.add_subplot(2, 3, 5)
ax4.title.set_text('np.int64')
cs = np.int64(co)
io.imshow(cs, cmap='gray', vmin=0, vmax=255)

ax = fig.add_subplot(2, 3, 6)
ax.title.set_text('np.float64')
cs = np.float64(co)
io.imshow(cs, cmap='gray', vmin=0, vmax=255)
io.show()
