from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import skimage.exposure as ex


# 평활화는 누적 히스토그램을 스트래칭함


plt.figure(figsize=(10, 6))

plt.subplot(2, 5, (1, 2))
img = io.imread('sample_Images/engineer.tif')
img = np.ubyte(img/4)
plt.title('original/4')
io.imshow(img)

plt.subplot(2, 5, (3, 5))
plt.hist(img.flatten(), bins=256, range=(0, 255))

plt.subplot(2, 5, (6, 7))
plt.title('equlization')
st = ex.equalize_hist(img)  # 0~1 float
io.imshow(st)

plt.subplot(2, 5, (8, 10))
plt.hist(st.flatten(), bins=256, range=(0, 1))

plt.tight_layout()
io.show()
