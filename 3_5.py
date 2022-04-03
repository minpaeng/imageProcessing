import matplotlib.pyplot as plt
import skimage.transform as tr
import skimage.util
from skimage import io
import numpy as np


def quantization():
    fig = plt.figure()

    c = io.imread('sample_Images/newborn.tif')
    c0 = np.uint8(c)
    c64 = np.uint8(np.floor(c0 / 4) * 4)
    c16 = np.uint8(np.floor(c0 / 16) * 16)
    c4 = np.uint8(np.floor(c0 / 64) * 64)

    a = fig.add_subplot(2, 2, 1)
    a.title.set_text('c0')
    plt.axis('off')
    io.imshow(c0)

    a = fig.add_subplot(2, 2, 2)
    a.title.set_text('c64')
    plt.axis('off')
    io.imshow(c64)

    a = fig.add_subplot(2, 2, 3)
    a.title.set_text('c16')
    plt.axis('off')
    io.imshow(c16)

    a = fig.add_subplot(2, 2, 4)
    a.title.set_text('c4')
    plt.axis('off')
    io.imshow(c4)

    io.show()


def pattern_dithering_4x4():
    x = io.imread('sample_Images/newborn.tif', as_gray=True)
    (n, m) = x.shape
    d = np.array([[0, 128, 32, 160], [192, 64, 224, 96],
                  [48, 176, 16, 144], [240, 112, 208, 80]])

    dx = np.tile(d, (n // 4 + 1, m // 4 + 1))[:n, :m]
    p = np.float32(x > dx)
    io.imshow(p)
    io.show()


def pattern_dithering_level8():
    x = io.imread('sample_Images/newborn.tif', as_gray=True)
    (n, m) = x.shape
    x = np.float64(x)
    q = np.floor(x / 37)
    d = np.array([[0, 24], [36, 12]])
    dx = np.tile(d, (n // 2 + 1, m // 2 + 1))[:n, :m]
    p = q + ((x - 37 * q) > dx)
    io.imshow(np.uint(37 * p), cmap='gray', vmin=0, vmax=255)
    io.show()


def fs(im, k):  # FS error diffusion at k levels
    print("image shape: {}".format(im.shape))                   # image shape: (256, 256)
    rs, cs = im.shape
    ed = np.array([[0, 0, 7], [3, 5, 1]]) / 16.0
    z = np.zeros((rs + 2, cs + 2))
    print("np.zeros: {}".format(z.shape))                       # np.zeros: (258, 258)
    z[1:rs + 1, 1:cs + 1] = np.array(im, dtype='float64')
    for i in range(1, rs + 1):
        for j in range(1, cs + 1):
            old = z[i, j]
            quant = (old // (255 // k)) * (255 // (k - 1))
            z[i, j] = quant
            E = old - quant
            z[i:i + 2, j - 1:j + 2] = z[i:i + 2, j - 1:j + 2] + E * ed
    return np.array(z[1:rs + 1, 1:cs + 1], dtype='uint8')


img = io.imread('sample_Images/newborn.tif', as_gray=True)
p = fs(img, 2)
io.imshow(p, cmap='gray', vmin=0, vmax=255)
io.show()

# quantization()
# pattern_dithering_4x4()
# pattern_dithering_level8()
