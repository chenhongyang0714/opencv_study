# opencv_study

opencv官方文档下载地址：https://docs.opencv.org/  
opencv官方文档在线学习：https://docs.opencv.org/master/d9/df8/tutorial_root.html

这30个文件夹与贾志刚老师30节课的教学视频相对应。这是我大一暑假期间跟着贾志刚老师学习 opencv 时手敲的代码，基本每一行难懂的地方都添加了注释。如果大家对这份资料有任何疑问，可以发 Issues
或者在 b 站发评论。(一个大一学生都可以看明白的代码，你当然可以)


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
010.高斯模糊 | 1. 添加高斯噪声; | 高斯模糊API (可抑制高斯噪声)(保留图像的主要特征) | np.random.normal()、cv.GaussianBlur()
011.边缘保留滤波(EPF) | 1. 高斯双边模糊(保存图像边缘细节); 2. 均值迁移滤波; |  cv.bilateralFilter()、cv.pyrMeanShiftFiltering()
012.图像直方图(histogram) | 1. 直方图(反应图像的主要特征); 2.构造曲线图(三通道)  |  cv.calcHist()、plt.hist()、cv.calcHist()
013.直方图应用 | 1. 全局直方图均衡化(增强图像对比度);  2. 局部直方图均衡化(可调 对比度大小); 3.  做一个RGB的直方图; 4.数据比较(巴氏距离、相关性、卡方) | cv.equalizeHist()、	cv.createCLAHE()、cv.compareHist()
014.直方图反向投影 | 1.直方图的反向衍射(反向投影); 2.设计2D直方图 | cv.normalize()、cv.calcBackProject()
015.模块匹配 | 1. 平方不同、相关性、相关性因子的 归一化; 2. 绘制矩形边框 | cv.matchTemplate()、cv.minMaxLoc()、cv.rectangle()



