# -*- coding: utf-8 -*-
import cv2
import numpy as np

picture = cv2.imread("color.png", 1)
hsv = cv2.cvtColor(picture, cv2.COLOR_BGR2HSV)
# 设定绿色的阈值
lower_green = np.array([-40, 100, 100])
upper_green = np.array([160, 255, 255])
# 根据阈值构建掩模
mask = cv2.inRange(hsv, lower_green, upper_green)
# 队员图像和掩模进行位运算
res = cv2.bitwise_and(picture, picture, mask=mask)

# 显示图像
cv2.imshow("picture", picture)
cv2.imshow("mask", mask)
cv2.imshow("res", res)
k = cv2.waitKey(0)

# lower_green = np.array()
# green = np.uint8([[[0, 255, 0]]])
# hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)  # [[[ 60 255 255]]]
#
# print(hsv_green)
