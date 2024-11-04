import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import shutil




def norm(image, base=160):
    # image = image.astype(np.float32)
    # image -= np.mean(image)
    # max_, min_ = image.max(), image.min()
    # print(max_, min_)
    # if max_ != min_:
    #     image = (image - min_) / (max_ - min_)
    # return image
    errormap = np.zeros(image.shape)
# errormap = np.abs(img-disp_gt)
    errormap[image > base+70] = 240
    #errormap[(image > 170) & (image < 180)] = 220
    errormap[(image > base+60) & (image < base+70)] = 200
    errormap[(image > base+50) & (image < base+60)] = 160
    errormap[(image > base+40) & (image < base+50)] = 150
    errormap[(image > base+30) & (image < base+40)] = 140
    errormap[(image > base+25) & (image < base+30)] = 130
    errormap[(image > base+20) & (image < base+25)] = 120
    errormap[(image > base+10) & (image < base+20)] = 110
    errormap[(image > base) & (image < base+10)] = 100
    # errormap[image > 140] = 255
    errormap[(image > 0) & (image < base)] = 0
    return errormap
# 定义输入和输出目录
image_dir = 'cave'
base= 10
output_dir = '%s_heat' % image_dir

# 如果输出目录存在，清空目录；如果不存在，创建目录
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

# 读取目录下的所有图像文件
image_files = [f for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.tif'))]

for image_file in image_files:
    # 读取图像
    image_path = os.path.join(image_dir, image_file)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 归一化到0-1
    # normalized_image = cv2.normalize(image, None, 0, 1, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    normalized_image = norm(image, base=base)
    """ cv2.COLORMAP_AUTUMN: 秋天映射，颜色从红到黄。
        cv2.COLORMAP_BONE: 骨骼映射，灰度图像。
        cv2.COLORMAP_JET: JET 映射，颜色从蓝到红。
        cv2.COLORMAP_WINTER: 冬天映射，颜色从蓝到绿色。
        cv2.COLORMAP_RAINBOW: 彩虹映射，颜色从红到紫。
        cv2.COLORMAP_OCEAN: 海洋映射，颜色从蓝到绿色。
        cv2.COLORMAP_SUMMER: 夏天映射，颜色从绿色到黄色。
        cv2.COLORMAP_SPRING: 春天映射，颜色从洋红到黄。
        cv2.COLORMAP_COOL: 冷色映射，颜色从青到洋红。
        cv2.COLORMAP_HSV: HSV 映射，颜色从红到紫。
        cv2.COLORMAP_PINK: 粉色映射，颜色从浅粉到白。
        cv2.COLORMAP_HOT: 热映射，颜色从黑到红、黄、白。
        cv2.COLORMAP_PARULA: Parula 映射，颜色从蓝到黄。
        cv2.COLORMAP_MAGMA: Magma 映射，颜色从黑到红、黄。
        cv2.COLORMAP_INFERNO: Inferno 映射，颜色从黑到红、黄。
        cv2.COLORMAP_PLASMA: Plasma 映射，颜色从黑到红、黄。
        cv2.COLORMAP_VIRIDIS: Viridis 映射，颜色从蓝到绿、黄。
        cv2.COLORMAP_CIVIDIS: Cividis 映射，颜色从蓝到黄。
        cv2.COLORMAP_TWILIGHT: Twilight 映射，颜色从蓝到红。
        cv2.COLORMAP_TWILIGHT_SHIFTED: Twilight Shifted 映射，颜色从蓝到红。
        cv2.COLORMAP_TURBO: Turbo 映射，颜色从蓝到红、黄。
        cv2.COLORMAP_DEEPGREEN: Deep Green 映射，颜色从黑到绿。
    """
    # 转为热力图
    heatmap = cv2.applyColorMap((normalized_image).astype(np.uint8), cv2.COLORMAP_WINTER)
    
    # 保存热力图
    heatmap_path = os.path.join(output_dir, f'heatmap_{image_file}')
    cv2.imwrite(heatmap_path, heatmap)
    
    # 显示热力图
    # plt.imshow(heatmap)
    # plt.title(f'Heatmap of {image_file}')
    # plt.axis('off')
    # plt.show()