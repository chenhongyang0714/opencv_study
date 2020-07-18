import cv2 as cv
import numpy as np  # Python的一种开源的数值计算扩展包


def get_image_info(image):  # 获取图像信息的函数
    print(type(image))  # 获取其数据类型(n维数组类型)
    print(image.shape)  # 高度 宽度 通道数
    print(image.size)  # 总的像素数据（高度 * 宽度 * 通道数）
    print(image.dtype)  # 每个像素点有3个通道 每个通道占的位数是 无符号的int的8位

    pixel_data = np.array(image)  # 获取所有像素数据
    print(pixel_data)


print("-------Hello World-------")
scr = cv.imread("yuanyuan.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", scr)

get_image_info(scr)

# gray = cv.cvtColor(scr, cv.COLOR_BGR2GRAY)  # 转化成灰色照片
# cv.imwrite("gao11.png", gray)  # 新照片的名字  写入到当前文件夹

cv.waitKey(0)
cv.destroyAllWidows()
