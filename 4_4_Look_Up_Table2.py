from skimage import io
import matplotlib.pyplot as plt
import numpy as np


# 대비 스트레칭 함수를 LUT로 구현: 3단계 부분 선형 스트레칭
plt.figure(figsize=(10, 6))

plt.subplot(2, 5, (1, 2))
img = io.imread('sample_Images/engineer.tif')
plt.title('original')
io.imshow(img)

plt.subplot(2, 5, (3, 5))
plt.hist(img.flatten(), bins=256, range=(0, 255))


# 룩업 테이블
LUT = []
for x in range(0,96):
    LUT.append(int(0.6667*x))
for x in range(96,160):
    LUT.append(int(2*x-128))
for x in range(160,256):
    LUT.append(int(0.6632*x+85.8947))
LUT = np.ubyte(LUT)


plt.subplot(2, 5, (6, 7))
plt.title('3 piecewise')
st = LUT[img]
io.imshow(st)

plt.subplot(2, 5, (8, 10))
plt.hist(st.flatten(), bins=256, range=(0, 256))

plt.tight_layout()
io.show()
