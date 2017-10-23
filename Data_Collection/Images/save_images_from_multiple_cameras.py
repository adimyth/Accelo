import cv2
import numpy as np
import imutils
import os
from imutils.video import VideoStream

frames_list_1 = []
frames_list_2 = []
frames_list_3 = []

cap_1 = cv2.VideoCapture(0)
cap_1.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
cap_1.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)

cap_2 = cv2.VideoCapture(1)
cap_2.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
cap_2.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)

cap_3 = cv2.VideoCapture(2)
cap_3.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
cap_3.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)

while True:
	ret_1, frame_1 = cap_1.read()
	ret_2, frame_2 = cap_2.read()
	ret_3, frame_3 = cap_3.read()

	(h,w) = frame_1.shape[:2]
	zeros = np.zeros((h, w), dtype="uint8")
	output = np.zeros((h * 2, w * 2, 3), dtype="uint8")
	output[0:h, 0:w] = frame_1
	output[0:h, w:w * 2] = frame_2
	output[h:h * 2, w:w * 2] = frame_3
	output[h:h * 2, 0:w] = frame_1
	cv2.imshow("Output", output)

	frames_list_1.append(frame_1)
	frames_list_2.append(frame_2)
	frames_list_3.append(frame_3)

	if cv2.waitKey(1) == ord('q'):
		break

directory_1 = 'Front_Camera_1' 
if not os.path.exists(directory_1):
	os.mkdir(directory_1)
for ctr,image in enumerate(frames_list_1):
	name = 'Front_Camera_1_'+str(ctr)+'.jpg'
	cv2.imwrite('Front_Camera_1/'+ name, image)

directory_2 = 'Front_Camera_2' 
if not os.path.exists(directory_2):
	os.mkdir(directory_2)
for ctr,image in enumerate(frames_list_2):
	name = 'Front_Camera_2_'+str(ctr)+'.jpg'
	cv2.imwrite('Front_Camera_2/'+ name, image)

directory_3 = 'Back_Camera' 
if not os.path.exists(directory_3):
	os.mkdir(directory_3)
for ctr,image in enumerate(frames_list_1):
	name = 'Back_Camera_'+str(ctr)+'.jpg'
	cv2.imwrite('Back_Camera/'+ name, image)

cap_1.release()
cap_2.release()
cap_3.release()
cv2.destroyAllWindows()