from skimage import io
import matplotlib.pyplot as plt
import numpy as np


def stucki(im, k):
    # print("image shape: {}".format(im.shape))                   # image shape: (256, 256)
    rs, cs = im.shape
    ed = np.array([[0, 0, 0, 8, 4], [2, 4, 8, 4, 2], [1, 2, 4, 2, 1]]) / 42.0
    z = np.zeros((rs + 4, cs + 4))
    # print("np.zeros: {}".format(z.shape))                       # np.zeros: (260, 260)
    z[2:rs + 2, 2:cs + 2] = np.array(im, dtype='float64')
    for i in range(2, rs + 2):
        for j in range(2, cs + 2):
            old = z[i, j]
            quant = (old // (255 // k)) * (255 // (k - 1))
            z[i, j] = quant
            E = old - quant
            z[i:i + 3, j - 2:j + 3] = z[i:i + 3, j - 2:j + 3] + E * ed
    return np.array(z[2:rs + 2, 2:cs + 2], dtype='uint8')


fig = plt.figure()

img = io.imread('sample_Images/newborn.tif', as_gray=True)

s = stucki(img, 2)
a = fig.add_subplot(111)
a.title.set_text('stucki(k = 2)')
plt.axis('off')
io.imshow(s, cmap='gray', vmin=0, vmax=255)
io.show()
