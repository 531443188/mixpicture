# -*- coding: utf-8 -*-
import cv2
import numpy as np


def pull2back(img_pull, img_back, center, rows, cols):
    # img_pull 需要抠图的图片，img_back 背景图片  center 在背景图片中的位置 rows图片的行数 cols图片的列数
    # 转换hsv
    hsv = cv2.cvtColor(img_pull, cv2.COLOR_BGR2HSV)
    # 获取mask
    lower_blue = np.array([78, 43, 46])
    upper_blue = np.array([110, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # 腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)
    dilate = cv2.dilate(erode, None, iterations=1)
    cv2.imshow('dilate', dilate)
    # 遍历替换
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 0:  # 0代表黑色的点
                img_back[center[0] + i, center[1] + j] = img_pull[i, j]  # 此处替换颜色，为BGR通道
    return img_back


img = cv2.imread('123.png')  # 读取出来的是Numpy阵列
img2 = cv2.imread('333.png')
img_back = cv2.imread('grass.png')

img_back = cv2.resize(img_back, None, fx=0.7, fy=0.7)
rows_back, cols_back, channels_back = img_back.shape
image_bak = img_back

img2 = cv2.resize(img2, None, fx=0.4, fy=0.4)
rows, cols, channels = img2.shape
center = [int(rows_back - rows), 200]  # 行数y，列数x
img_back = pull2back(img2, img_back, center, rows, cols)  # 进行抠图移植

img = cv2.resize(img, None, fx=0.3, fy=0.3)
rows, cols, channels = img.shape  # 获取图片对应行列，在背景图片中进行替换使用
center = [int(rows_back - rows), 200]
img_back = pull2back(img, img_back, center, rows, cols)  # 进行抠图移植

cv2.imshow('res', img_back)
cv2.waitKey(0)
# 访问图片位于100，100像素点的BGR的值
px = img[100, 100]
# 打印所有蓝色像素点
blue = img[0, 0, 0]
