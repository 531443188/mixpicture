# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib

BLUE = [255, 0, 0]
picture = cv2.imread("test.jpg", cv2.IMREAD_COLOR)  # 彩色模式 1 默认模式
# px = picture[20, 20]
# print(picture.item(10, 10, 2))
# picture.itemset((10,10,2),100)
replicate = cv2.copyMakeBorder(picture, 10, 10, 10, 10, cv2.BORDER_WRAP)
cv2.imshow("picture", replicate)
cv2.waitKey(0)

# print(picture.item(10, 10, 2))
