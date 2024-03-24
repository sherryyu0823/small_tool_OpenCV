import numpy as np
import matplotlib.pyplot as plt
import cv2

row = cv2.imread('img_path.png')
print(row.shape)
# Set the frame size you want
# 20 here means the strides moving per frame(you can change it anyway)
row_p = np.zeros((300,300,3,20), dtype='uint8')
h,w,d,N = row_p.shape


img = cv2.imread('img_path.png',0)
out = cv2.VideoWriter('video_path.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 10, (w,h))
print(N)
for i in range(N):

     row_p[:,:,:,i] = row[60-3*i:360-3*i,300:600,:]
     cv2.imshow("img_path.png",row_p[:,:,:,i])
     out.write(row_p[:,:,:,i])
videoWriter.release()
