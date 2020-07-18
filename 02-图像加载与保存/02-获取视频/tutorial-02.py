import cv2 as cv


def video_demo():
    capture = cv.VideoCapture(0)  # 从摄像头中进行视频的获取
    while True:
        ret, frame = capture.read(0)  # ret 为True 或者False,代表有没有读取到视频。  frame为视频的每一帧
        frame = cv.flip(frame, 1)  # 图像翻转(0是垂直方向，1是水平方向，-1是垂直、水平方向同时反转)
        cv.imshow("video", frame)
        c = cv.waitKey(50)  # 50ms 刷新屏幕图像一次
        if c == 48:  # 如果键入值为'0'(asc2)
            break


video_demo()

cv.waitKey(50)
cv.destroyAllWidows()


