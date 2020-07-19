# opencv_study

opencv官方文档下载地址：https://docs.opencv.org/  
opencv官方文档在线学习：https://docs.opencv.org/master/d9/df8/tutorial_root.html

这30个文件夹与贾志刚老师30节课的教学视频相对应。这是我大一暑假期间跟着贾志刚老师学习 opencv 时手敲的代码，基本每一行难懂的地方都添加了注释。如果大家对这份资料有任何疑问，可以发 Issues
或者在 b 站发评论。(一个大一学生都可以看明白的代码，你当然可以)

#### 运行环境
python3.7 + py-opencv3.4.2

#### 总结每一节课讲解的知识点以及所使用的opencv函数

课时 | 讲解的知识 | opencv 函数
:-: | :-: | :-: 
001.概述与环境搭建 | 创建一个GUI 进行相应位置图片的读取 | 
002.图像加载与保存 | 1. 获取图像信息(通道数目、宽度、高度、总的像素数据;  2. 将彩色照片转化为灰色照片并保存到相应地址 | np.array()、cv.imwrite()
002.图像加载与保存 | 1.  从电脑的摄像头进行视频的获取; 2.进行图像的翻转 | cv.VideoCapture()、cv.flip()
003.Numpy数组操作 | 1. 计算照片的宽、高、通道数; 2.  遍历每一个像素并修改像素的值; 3.  像素取反; 4. 时间计算 | cv.getTickCount()、cv.getTickFrequency()
003.Numpy数组操作 | 1. 初始化的两种方法 np.zeros()、np.ones(); 2. 多通道操作、单通道操作; 3. 创建数组(1)(2)、不同维度数组之间的转换; | cv.convertScaleAbs()、np.zeros()、np.ones()
004.色彩空间-01 | 色彩的相互转换 | 
005.色彩空间-02 | 1.读取视频并进行色彩筛选 inrange(); 2. 通道的分离; 3. 通道的合并 | cv.inRange() 用hsv返回gray、cv..split()、cv.merge()
006.像素运算-01 | 1. 像素的运算(加、减、乘、除、均值、方差) |  cv.add()、cv.subtract()、cv.multiply、cv.divide()、cv.meanStdDev()
007.像素运算-02 | 1. 逻辑与、或、非运算; 2.  对比度、亮度的调节  |  cv.bitwise_and()、cv.addWeighted()
008.ROI与泛洪填充 | 1. 进行face的ROI的选取，灰度之后再添加到原图像中; 2. 彩色图像的填充(泛洪填充); 3. 二值图像的填充 | cv.floodFill()
009.模糊操作 | 1. 均值模糊(对随机噪声有很好的去噪效果); 2. 中值模糊(去除椒盐噪声); 3. 自定义模糊; 4. 锐化(增强图像立体感) | cv.blur()、cv.medianBlur()、cv.filter2D()
010.高斯模糊 | 1. 添加高斯噪声; 2.高斯模糊API (可抑制高斯噪声)(保留图像的主要特征) | np.random.normal()、cv.GaussianBlur()
011.边缘保留滤波(EPF) | 1. 高斯双边模糊(保存图像边缘细节); 2. 均值迁移滤波; |  cv.bilateralFilter()、cv.pyrMeanShiftFiltering()
012.图像直方图(histogram) | 1. 直方图(反应图像的主要特征); 2.构造曲线图(三通道)  |  cv.calcHist()、plt.hist()、cv.calcHist()
013.直方图应用 | 1. 全局直方图均衡化(增强图像对比度);  2. 局部直方图均衡化(可调 对比度大小); 3.  做一个RGB的直方图; 4.数据比较(巴氏距离、相关性、卡方) | cv.equalizeHist()、	cv.createCLAHE()、cv.compareHist()
014.直方图反向投影 | 1.直方图的反向衍射(反向投影); 2.设计2D直方图 | cv.normalize()、cv.calcBackProject()
015.模块匹配 | 1. 平方不同、相关性、相关性因子的 归一化; 2. 绘制矩形边框 | cv.matchTemplate()、cv.minMaxLoc()、cv.rectangle()
016.图像二值化(黑白图像) | 1. 全局阀值; 2. 局部阀值 |  cv.threshold()、cv.adaptiveThreshold()、gray.sum()
017.超大图像二值化 | 1. 分块求图像二值化(全局阀值); 2. 分块求图像二值化(局部阀值)(优); 3.分块求图像二值化(全局阀值)(方差小于某个值时，统一一个颜色) | 
018.图像金字塔 | 1. 高斯金字塔 reduce; 2.  拉普拉斯金字塔 | cv.pyrDown()、cv.pyrUp()
019.图像梯度 | 1.Soble算子; 2.Scharr算子->  Soble算子的增强版; 3. 拉普拉斯算子(API); 4.拉普拉斯算子(自定义) | cv.Sobel()、cv.convertScaleAbs()、cv.addWeighted()、cv.Scharr()、cv.Laplacian()、cv.filter2D()
020.Canny边缘提取 | 1.Canny边缘提取算法(对噪声敏感); 2. 将提取的边缘用彩色显示出来 | cv.Canny()、cv.bitwise_and()
021.直线检测 | 1. 霍夫直线检测(通过坐标之间的转化求得)(画直线); 2.霍夫直线检测(直接调用API求得)(画线段) |  cv.HoughLines()、cv.HoughLinesP()、cv.line()
022.圆检测 | 1.霍夫圆检测 | cv.HoughCircles()、np.around()、cv.circle()
023.轮廓发现 | 1. 轮廓发现(通过cv.Canny获取边缘检测图像传入cv.findContours); 2. 轮廓发现(通过cv.threshold获取二值图像传入cv.findContours) |  cv.findContours()、cv.drawContours()
024.对象测量 | 1. 轮廓面积; 2.计算轮廓垂直边界最小矩形; 3.计算矩形的宽高比; 4.几何矩、利用几何矩求取重心坐标; 5.多边形逼近(图形形状检测) | cv.contourArea()、cv.boundingRect()、cv.moments()、cv.rectangle()、cv.circle()、cv.approxPolyDP()
025.膨胀与腐蚀 | 1. 腐蚀(灰度图像)、膨胀(灰度图像); 2. 腐蚀(彩色图像)、膨胀(彩色图像) |  cv.getStructuringElement()、cv.erode()、cv.dilate()
026.开闭操作 | 1. 开闭操作; 2.水平、垂直线的提取; 3.开操作去除背景斜线、噪点 | cv.getStructuringElement()、cv.morphologyEx()
027.其他形态学操作 | 1. 顶帽(灰度图像)、黑帽(灰度图像); 2.顶帽(二值图像)、黑帽(二值图像);3.基本梯度(二值图像)(相当于提取边框);4. 内部梯度、外部梯度;5.利用数组提高图片亮度 | cv.morphologyEx()、cv.add()
028.分水岭操作 | 1. 分水岭分割流程：图像->灰度->二值->距离变换->寻找种子->生成Marker->分水岭变换->输出 | cv.connectedComponents()、cv.watershed()
029.人脸检测 | 1. 图片检测人脸;2.视频检测人脸 | cv.CascadeClassifier()、face_detect.detectMultiScale()
030.案例-数字验证码识别 |  | 



























