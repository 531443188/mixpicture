# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 矩形
cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
np.array([[1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]], dtype=np.uint8)
# 圆形
cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
kernel = np.array([[0, 0, 1, 0, 0],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [0, 0, 1, 0, 0]], dtype=np.uint8)
# 十字形
cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
np.array([[0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0],
          [1, 1, 1, 1, 1],
          [0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0]], dtype=np.uint8)

# 形态学算子是侵蚀和膨胀
img = cv.imread('test.jpg', 0)
# kernel = np.ones((5, 5), np.uint8)  # 构建一个矩形5X5的结构元素，可构建不同形状用于适配图形
erosion = cv.erode(img, kernel, iterations=1)  # 侵蚀
# cv.imshow("erosion", erosion)
# cv.waitKey(0)

dilation = cv.dilate(img, kernel, iterations=1)  # 扩张
cv.imshow("dilation", dilation)
cv.waitKey(0)

opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)  # 开幕，扩大后侵蚀的名称
# cv.imshow("opening", opening)
# cv.waitKey(0)

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)  # 闭幕，侵蚀后扩大的名称
# cv.imshow("closing", closing)
# cv.waitKey(0)

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
# cv.imshow("gradient", gradient)
# cv.waitKey(0)

