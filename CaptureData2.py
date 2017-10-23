import sys, getopt
import numpy as np
import cv2
sys.path.append('.')
import os.path
import time
import math

cam1 = cv2.VideoCapture(1)
cam1.set(cv2.CAP_PROP_FRAME_WIDTH,1280);
cam1.set(cv2.CAP_PROP_FRAME_HEIGHT,720);

cam2 = cv2.VideoCapture(2)
cam2.set(cv2.CAP_PROP_FRAME_WIDTH,1280);
cam2.set(cv2.CAP_PROP_FRAME_HEIGHT,720);

cam3 = cv2.VideoCapture(3)
cam3.set(cv2.CAP_PROP_FRAME_WIDTH,1280);
cam3.set(cv2.CAP_PROP_FRAME_HEIGHT,720);


counter = 0

PATH = 'data_test/'

while True:
  saveList = []

  _, imgLeft = cam1.read()	
  _, imgRight = cam2.read()
  _, imgBack = cam3.read()

  saveList.append(imgLeft)
  saveList.append(imgRight)
  saveList.append(imgBack)
  
  np.save(PATH + 'out' + str(counter) + '.npy', saveList)
  counter += 1
