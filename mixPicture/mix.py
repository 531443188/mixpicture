# -*- coding: utf-8 -*-
from PIL import Image
from matplotlib import pyplot as plt

# 加载底图
base_img = Image.open('grass.png')
# 可以查看图片的size和mode，常见mode有RGB和RGBA，RGBA比RGB多了Alpha透明度
# print base_img.size, base_img.mode
box1 = (166, 64, 320, 337)  # 底图上需要P掉的区域1
box2 = (366,266,420,337)    # 底图上需要P掉的区域2

# 加载需要P上去的图片
tmp_img = Image.open('tree.png')
tmp_img2 = Image.open('123.png')
# 这里可以选择一块区域或者整张图片
# region = tmp_img.crop((0,0,304,546)) #选择一块区域
# 或者使用整张图片
region = tmp_img
region2 = tmp_img2
# 使用 paste(region, box) 方法将图片粘贴到另一种图片上去.
# 注意，region的大小必须和box的大小完全匹配。但是两张图片的mode可以不同，合并的时候回自动转化。如果需要保留透明度，则使用RGMA mode
# 提前将图片进行缩放，以适应box区域大小
# region = region.rotate(180) #对图片进行旋转
region = region.resize((box1[2] - box1[0], box1[3] - box1[1]))  #重新构建植入图片的长宽
region2 = region2.resize((box2[2] - box2[0], box2[3] - box2[1]))

base_img.paste(region, box1)  # 选择图片上植入另外一张图片的区域
base_img.paste(region2, box2)  # 选择图片上植入另外一张图片的区域

# 查看或者保存合成的图片
# base_img.save('./out.png')  # 保存图片
plt.imshow(base_img, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()