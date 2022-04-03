import skimage.exposure as ex
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15, 7))


# 히스토그램 스트래칭은 히스토그램 바 자체를 스트래칭함

# 원본
plt.subplot(2, 10, (1, 2))
img = io.imread('sample_Images/pout.tif')
plt.title('original')
io.imshow(img)

plt.subplot(2, 10, (3, 5))
plt.hist(img.flatten(), bins=256, range=(0, 256))


# default값: 입력 영상의 최소/최대 값이 입력 영상(uint8)의 데이터 타입의 최소/최대값으로 스트래칭됨
plt.subplot(2, 10, (6, 7))
plt.title('image->ubyte')
st = ex.rescale_intensity(img)
io.imshow(st)

plt.subplot(2, 10, (8, 10))
plt.hist(st.flatten(), bins=256, range=(0, 256))


# 입력 영상의 최소/최대 값이 float 타입인 0~1로 스트래칭됨
plt.subplot(2, 10, (11, 12))
plt.title('image->float')
st = ex.rescale_intensity(img, out_range=(0, 1))
io.imshow(st)

plt.subplot(2, 10, (13, 15))
plt.hist(st.flatten(), bins=256, range=(0, 1))


# 입력 영상의 80~170 구간에 해당하는 값이 0~255 구간으로 스트래칭됨
plt.subplot(2, 10, (16, 17))
plt.title('(80, 170)->(0, 255)')
st = ex.rescale_intensity(img, in_range=(80, 170), out_range=(0, 255))
io.imshow(np.ubyte(st), cmap='gray', vmin=0, vmax=255)

plt.subplot(2, 10, (18, 20))
plt.hist(st.flatten(), bins=256, range=(0, 256))


plt.tight_layout()
io.show()
