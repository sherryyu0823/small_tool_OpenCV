import cv2
import time
import os
videoWriter = cv2.VideoWriter('ambush.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 10, (1024,436))
# retval = cv.VideoWriter.open(filename, fourcc, fps, frameSize[, isColor])
# - 保存视频为test.avi，可以选择mp4等
# - fps为25,即每秒25张图片
# - 视频尺寸大小为1920,1080
# - isColor可以为true,flase选择是否有颜色
for filename in os.listdir("./ambush_2"):
    print(filename)
    img = cv2.imread("./ambush_2/"+filename)
# for i in range(1,21):
    # 加载图片，图片更多可以改变上面的10
    # img  = cv2.imread('./ambush_2/frame_00'+str(i)+'.png')
    img = cv2.resize(img,(1024,436))
    # 如果每张图片为只显示一下，就用如下代码
    videoWriter.write(img)
for filename in os.listdir("./ambush_4"):
    print(filename)
    img = cv2.imread("./ambush_4/"+filename)
# for i in range(1,21):
    # 加载图片，图片更多可以改变上面的10
    # img  = cv2.imread('./ambush_2/frame_00'+str(i)+'.png')
    img = cv2.resize(img,(1024,436))
    # 如果每张图片为只显示一下，就用如下代码
    videoWriter.write(img)
for filename in os.listdir("./ambush_5"):
    print(filename)
    img = cv2.imread("./ambush_5/"+filename)
    img = cv2.resize(img,(1024,436))
    videoWriter.write(img)
videoWriter.release()