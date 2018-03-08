# -*- coding: utf-8 -*-
'''图像阈值使用'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''简单阈值使用'''
# img = cv.imread('dog.png', 0)
# ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  # 超过阈值设置为最大值，其余为0
# ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)  # 超过阈值设置为0，其余为最大值
# ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)  # 超过阈值设置为阈值，其余不变
# ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)  # 超过阈值不变，其余为0
# ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)  # 超过阈值为0，其余不变
# titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(0, 6):
#     plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()

'''自适应阈值使用'''
# img = cv.imread('dog.png', 0)
# img = cv.medianBlur(img, 5)
#
# ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
# th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
#
# titles = ['Original Image', 'Global Thresholding (v = 127)',
#           'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
#
# for i in range(0, 4):
#     plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()

'''大津的二元化'''
# img = cv.imread('noisy.png', 0)
#
# # global thresholding
# ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
#
# # Otsu's thresholding
# ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
#
# # Otsu's thresholding after Gaussian filtering
# blur = cv.GaussianBlur(img, (5, 5), 0)
# ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
#
# # plot all the images and their histograms
# images = [img, 0, th1, img, 0, th2, blur, 0, th3]
# titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
#           'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
#           'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
#
# for i in range(3):
#     plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
#     plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
#     plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
#     plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
# plt.show()
img = cv.imread('noisy.png', 0)
blur = cv.GaussianBlur(img, (5, 5), 0)

# find normalized_histogram, and its cumulative distribution function
hist = cv.calcHist([blur], [0], None, [256], [0, 256])
hist_norm = hist.ravel() / hist.max()
Q = hist_norm.cumsum()

bins = np.arange(256)

fn_min = np.inf
thresh = -1

for i in range(1, 256):
    p1, p2 = np.hsplit(hist_norm, [i])  # probabilities
    q1, q2 = Q[i], Q[255] - Q[i]  # cum sum of classes
    b1, b2 = np.hsplit(bins, [i])  # weights

    # finding means and variances
    m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
    v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2

    # calculates the minimization function
    fn = v1 * q1 + v2 * q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

# find otsu's threshold value with OpenCV function
ret, otsu = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
print("{} {}".format(thresh, ret))
