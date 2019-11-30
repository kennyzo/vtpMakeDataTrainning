import cv2
import time
import os
vidcap = cv2.VideoCapture('source_videos/20191129_M02_08h39.mp4')
success,image = vidcap.read()
count = 0
path = "source_images" + "/20191129_M02_08h39"
os.mkdir(path)
while success:
  cv2.imwrite(path + "/20191129_M02_08h39-%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  #time.sleep()
  count += 1

