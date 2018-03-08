# -*- coding: utf-8 -*-
import cv2

def gray_picture(input_path, output_path):
    # imread需要读进完整的一张图 是128*128*4维的图片 多的一维是alpha通道就是透明度
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)  #
    if img is not None:
        # 因为灰度模式下透明信息被舍弃，原来透明的像素点值为0，也就是变成了黑色（白色为255）
        # img[:,:,3] = 255
        # 对所有透明度作画的图片转成实际颜色处理
        # 遍历img，把透明度转化为实际颜色
        if img.shape[2] > 3:  # 通道数判断
            b, g, r, a = cv2.split(img)  # 4通道
            # 透明图片作画的处理，透明画的特点是bgr都为0，a上有值
            if (b == g).all() and (b == r).all() and (r == g).all():
                a_img = a  # 取透明通道
                for i in range(len(a_img)):
                    a_img[i] = 255 - a_img[i]
                    for j in range(len(a_img[i])):
                        if int(a_img[i][j]) > 128:
                            a[i][j] = 255
                        else:
                            a[i][j] = 0
                new_img = a_img
            else:
                new_img = cv2.merge([b, g, r])
                new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)  # 转换了灰度化+
        else:
            new_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换了灰度化+

        # 用高斯平滑处理原图像降噪
        new_img = cv2.GaussianBlur(new_img, (3, 3), 0)
        # 最外一层1px做外围涂白色，使得内容封闭
        new_img = new_img[1:-1, 1:-1]
        new_img = cv2.copyMakeBorder(new_img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=255)
        # 用canny特征提取轮廓
        new_img = cv2.Canny(new_img, 50, 150)
        # 图像取反
        new_img = 255 - new_img
        # 保存图片
        cv2.imwrite(output_path, new_img)
    else:
        print("图片读取失败，请检测是否上传成功")
