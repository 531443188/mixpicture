# -*- coding: utf-8 -*-

import cv2

# picture = cv2.imread("color.png", cv2.IMREAD_COLOR)  # 彩色模式 1 默认模式
picture = cv2.imread("color.png", cv2.IMREAD_GRAYSCALE)  # 灰度模式 0
# picture = cv2.imread("color.png", cv2.IMREAD_UNCHANGED)  # 全读取 -1 png、gif、TIFF、PSD都是带有透明度的图片
if len(picture.shape) == 2:
    row, col = picture.shape  # 返回行数，列数 为灰度图
else:
    row, col, channels = picture.shape  # 返回行数，列数 为灰度图
print(picture.dtype)  # 打印图片的数据类型，可进行检测校验
cv2.imshow('image', picture)
cv2.waitKey(0)
cv2.destroyAllWindows()
b, g, r, a = None, None, None, None  # 蓝色，绿色，红色，Alph通道
if picture is not None:
    if channels == 3:  # 分割合并通道费时操作，其他情况一般使用Numpy索引
        b, g, r = cv2.split(picture)
        img = cv2.merge(b, g, r)
    elif channels == 4:
        b, g, r, a = cv2.split(picture)
        img = cv2.merge(b, g, r, a)
    print(picture)
else:
    print("图片为空!请检查是否图片路径错误。")
