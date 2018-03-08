# -*- coding: utf-8 -*-
import cv2
from glob import glob
import os
import copy

def pro_image2npy(image_path, input_fname_pattern):
    data = glob(os.path.join('./image', image_path, input_fname_pattern))
    imreadImg = cv2.imread(data[0], -1)  # 打开图像
    if imreadImg.shape[2] == 4:
        print('四通道进行分割')
        b, g, r, a = cv2.split(imreadImg)  # 在opencv中是b,g,r,a
        imreadImg = cv2.merge([r, g, b])  # 实际需要调整为r，g，b
        a_img = a  # 取透明通道
        for i in range(len(a_img)):
            a_img[i] = 255 - a_img[i]  # 取反，将透明通道做透明部分去除掉
            for j in range(len(a_img[i])):
                if int(a_img[i][j]) > 128:
                    a[i][j] = 255
                else:
                    a[i][j] = 0
        for i in range(len(a_img)):
            for j in range(len(a_img[i])):
                if int(a_img[i][j]) == 255:
                    imreadImg[i, j] = a_img[i][j]
    All_image = list()
    # 进行图像缩放，分别使用不同的函数
    methods = [
        ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
        ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
        ("cv2.INTER_AREA", cv2.INTER_AREA),
        ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
        ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
    count = 0
    original_image = list()
    original_image.append(imreadImg)
    iLR = copy.deepcopy(imreadImg)  # 镜像变换
    for i in range(400):
        for j in range(400):
            iLR[i, 400 - 1 - j] = imreadImg[i, j]
    original_image.append(iLR)
    for img in original_image:
        for x in range(4):
            M = cv2.getRotationMatrix2D((200, 200), 90, 1)
            img = cv2.warpAffine(img, M, (400, 400))
            for (name, method) in methods:
                dst = cv2.resize(img, None, fx=0.16, fy=0.16, interpolation=method)
                All_image.append(dst)
                count = count + 1
    while len(All_image) * 2 < 7370:
        All_image.extend(All_image)
    while len(All_image) < 7370:
        All_image.append(dst)
    np.save("train_images.npy", All_image)  # 生成对应的npy文件