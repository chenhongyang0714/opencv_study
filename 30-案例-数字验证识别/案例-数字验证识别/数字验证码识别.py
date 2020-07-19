import cv2 as cv
from PIL import Image
import pytesseract as tess


# 数字验证码识别
def recognize_text():
    dst = cv.pyrMeanShiftFiltering(src, 45, 55)  # 高斯模糊 空间窗的半径  色彩窗的半径
    dst1 = cv.bilateralFilter(dst, 0, 80, 15)  # 均值滤波
    # 二值化操作
    gray = cv.cvtColor(dst1, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # 形态学操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    open_out = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow("binary_image", open_out)

    # 格式转换
    cv.bitwise_not(open_out, open_out)  # 黑白色转换
    textImage = Image.fromarray(open_out)  # 实现array到image的转换
    text = tess.image_to_string(textImage)  # image 到 text
    print("识别结果：%s" % text)


print("------Hello------")
src = cv.imread("example1.jpg")
cv.imshow("image", src)

recognize_text()

cv.waitKey(0)
cv.destroyAllWindows()
