import cv2
import numpy as np
import imutils
import os
from imutils.video import VideoStream

frames_list_1 = []
frames_list_2 = []
frames_list_3 = []

# Codecs as per requirement
fourcc = cv2.VideoWriter_fourcc(*'XVID')

cap_1 = cv2.VideoCapture(0)
cap_1.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
cap_1.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)

cap_2 = cv2.VideoCapture(1)
cap_2.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
cap_2.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)

cap_3 = cv2.VideoCapture(2)
cap_3.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
cap_3.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)

# fps, frame_size
out_1 = cv2.VideoWriter('Front_Camera_1.avi',fourcc, 20.0, (640,480))
out_2 = cv2.VideoWriter('Front_Camera_2.avi',fourcc, 20.0, (640,480))
out_3 = cv2.VideoWriter('Back_Camera.avi',fourcc, 20.0, (640,480))

while True:
	ret_1, frame_1 = cap_1.read()
	ret_2, frame_2 = cap_2.read()
	ret_3, frame_3 = cap_3.read()

	cv2.imshow("Front Camera 1", frame_1)
	cv2.imshow("Front Camera 2", frame_2)
	cv2.imshow("Back Camera", frame_3)

	(h,w) = frame_1.shape[:2]

	frames_list_1.append(frame_1)
	frames_list_2.append(frame_2)
	frames_list_3.append(frame_3)

	out_1.write(frame_1)
	out_2.write(frame_2)
	out_3.write(frame_3)

	if cv2.waitKey(1) == ord('q'):
		break

cap_1.release()
cap_2.release()
cap_3.release()
cv2.destroyAllWindows()