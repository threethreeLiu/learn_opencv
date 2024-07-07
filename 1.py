"""
@File    : 1.py
@Date    : 2024-07-07
@Author  : ThreeThreeLiu
@Software : learn_opencv
Introduction to Image Course 1
cv.IMREAD_COLOR：默认参数，以彩色模式加载图像，图像的透明度将被忽略 0
cv.IMREAD_GRAYSCALE：以灰度模式加载图像。 - cv.IMREAD_UNCHANGED：以alpha通道模式加载图像 -1

"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/lts/Pictures/_DSC3025.jpg')
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
