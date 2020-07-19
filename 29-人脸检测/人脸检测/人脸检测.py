import cv2 as cv
import numpy as np


# 图片检测人脸
def face_detect_picture_demo():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier("D:/App Document/Anaconda/Library/etc/haarcascades/haarcascade_frontalface_alt_tree.xml")  # 级联分类器
    faces = face_detect.detectMultiScale(gray, 1.02, 5)  # 人脸检测
    for x, y, w, h in faces:
        cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("face_detect_picture_demo", src)


# 视频检测人脸
def face_detect_video_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier("D:/App Document/Anaconda/Library/etc/lbpcascades/lbpcascade_frontalcatface.xml")  # 级联分类器
    faces = face_detect.detectMultiScale(gray, 1.03, 5)  # 人脸检测
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("face_detect_video_demo", image)


print("------Hello------")
src = cv.imread("example.jpg")
# cv.imshow("image", src)

# 图片检测人脸
# face_detect_picture_demo()

# 视频检测人脸
capture = cv.VideoCapture(0)
while True:
    ret, frame = capture.read()  # 读取视频的每一帧
    # frame = cv.flip(frame, 1)  # 镜像转换
    face_detect_video_demo(frame)
    c = cv.waitKey(10)
    if c == 27:  # ESC
        break

cv.waitKey(0)
cv.destroyAllWindows()
