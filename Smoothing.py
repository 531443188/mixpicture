# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# img = cv.imread('opencv_logo.png')
# kernel = np.ones((5, 5), np.float32) / 25   # 5x5 = 25 个像素点
# dst = cv.filter2D(img, -1, kernel)
# plt.subplot(121), plt.imshow(img), plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()
img = cv.imread('opencv_logo.png')
img2 = cv.imread('opencv_logo2.png')    # 椒盐噪音图片
blur = cv.blur(img, (5, 5))  # 平均模糊
GaussianBlur = cv.GaussianBlur(img, (5, 5), 0)  # 高斯模糊
median = cv.medianBlur(img2, 5)  # 中位数模糊

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(GaussianBlur), plt.title('GaussianBlur')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(median), plt.title('median')
# plt.xticks([]), plt.yticks([])
plt.show()
