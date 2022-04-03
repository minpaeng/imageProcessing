from skimage import io
import matplotlib.pyplot as plt
import numpy as np


plt.figure(figsize=(10, 6))

plt.subplot(2, 5, (1, 2))
img = io.imread('sample_Images/engineer.tif')
plt.title('original')
io.imshow(img)

plt.subplot(2, 5, (3, 5))
plt.hist(img.flatten(), bins=256, range=(0, 255))


# 룩업 테이블
LUT = np.ubyte(np.arange(256) / 2)


plt.subplot(2, 5, (6, 7))
plt.title('LUT: 0.5')
st = LUT[img]
io.imshow(st)

plt.subplot(2, 5, (8, 10))
plt.hist(st.flatten(), bins=256, range=(0, 256))

plt.tight_layout()
io.show()
