import numpy as np
import cv2
import os 

dir_name = 'data' 

for file in os.listdir(dir_name):
    arr = np.load(os.path.join(dir_name,file))
    imgLeft = arr[0]
    #print 'Before'
    imgRight = arr[1]
    #fusion = arr[2]
    #accel = arr[3]
    #gyro = arr[4]

    cv2.imshow('left', imgLeft)
    cv2.waitKey(0)

    cv2.imshow('right', imgRight)
    #print '[GYRO] :',gyro 
    #print '[ACCEL] :',accel
    #print '[FUSION] :',fusion
