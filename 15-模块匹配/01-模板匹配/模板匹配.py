import cv2 as cv
import numpy as np


def template_demo():
    tpl = cv.imread("template1.jpg")
    target = cv.imread("target1.jpg")
    cv.imshow("image1", tpl)
    cv.imshow("target", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]  # 平方不同的归一化(优)  相关性的归一化 相关性因子的归一化
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)  # 打印出来是 枚举类型的值：1 3 5
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)
        cv.rectangle(target, tl, br, (0, 0, 255), 2)  # 画出一个红色的矩形   颜色、宽度
        cv.imshow("match"+np.str(md), target)


print("----------Hello World-----------")

template_demo()
cv.waitKey(0)