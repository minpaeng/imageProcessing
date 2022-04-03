import matplotlib.pyplot as plt
from skimage import io
import numpy as np
fig = plt.figure()

c = io.imread("sample_Images/cameraman.tif", as_gray=True, plugin='matplotlib')
cd = np.float64(c)

c0 = np.fmod(cd, 2)
c1 = np.fmod(np.floor(cd/2), 2)
c2 = np.fmod(np.floor(cd/2**2), 2)
c3 = np.fmod(np.floor(cd/2**3), 2)
c4 = np.fmod(np.floor(cd/2**4), 2)
c5 = np.fmod(np.floor(cd/2**5), 2)
c6 = np.fmod(np.floor(cd/2**6), 2)
c7 = np.fmod(np.floor(cd/2**7), 2)

ax1 = fig.add_subplot(2, 4, 1)
io.imshow(c0)

ax2 = fig.add_subplot(2, 4, 2)
io.imshow(c1)

ax3 = fig.add_subplot(2, 4, 3)
io.imshow(c2)

ax4 = fig.add_subplot(2, 4, 4)
io.imshow(c3)

ax5 = fig.add_subplot(2, 4, 5)
io.imshow(c4)

ax6 = fig.add_subplot(2, 4, 6)
io.imshow(c5)

ax7 = fig.add_subplot(2, 4, 7)
io.imshow(c6)

ax8 = fig.add_subplot(2, 4, 8)
io.imshow(c7)

io.show()
