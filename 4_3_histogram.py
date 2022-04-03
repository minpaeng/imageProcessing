from skimage import io
import matplotlib.pyplot as plt

plt.figure(figsize=(11, 5))
plt.subplot(1, 5, (1, 2))
img = io.imread('sample_Images/pout.tif')
plt.title('original')
io.imshow(img)

plt.subplot(1, 5, (3, 5))
plt.hist(img.flatten(), bins=256, range=(0, 256))
plt.title('histogram')
plt.tight_layout()
io.show()
