import matplotlib.pyplot as plt
import skimage.transform as tr
from skimage import io

fig = plt.figure()

x0 = io.imread('sample_Images/newborn.tif', as_gray=True)  # 256x256
a = fig.add_subplot(2, 2, 1)
a.title.set_text('x0')
plt.axis('off')
io.imshow(x0)

x4 = tr.rescale(tr.rescale(x0, 1 / 4), 4)  # 64x64
a = fig.add_subplot(2, 2, 2)
a.title.set_text('x4')
plt.axis('off')
io.imshow(x4)

x16 = tr.rescale(tr.rescale(x0, 1 / 16), 16)  # 16x16
a = fig.add_subplot(2, 2, 3)
a.title.set_text('x16')
plt.axis('off')
io.imshow(x16)

x64 = tr.rescale(tr.rescale(x0, 1 / 64), 64)  # 4x4
a = fig.add_subplot(2, 2, 4)
a.title.set_text('x64')
plt.axis('off')
io.imshow(x64)

io.show()
