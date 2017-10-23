from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2

vs_1 = VideoStream(1).start()
vs_2 = VideoStream(2).start()
vs_3 = VideoStream(3).start()

fourcc = cv2.VideoWriter_fourcc(*'X264')
writer_1 = None
writer_2 = None
writer_3 = None
(h, w) = (None, None)
zeros = None

while True:
	frame_1 = vs_1.read()
	frame_2 = vs_2.read()
	frame_3 = vs_3.read()

 	frame_1 = imutils.resize(frame_1, width=300)
 	frame_2 = imutils.resize(frame_2, width=300)
 	frame_3 = imutils.resize(frame_3, width=300)

	if writer_1 is None or writer_2 is None or writer_3 is None:
		(h, w) = frame_1.shape[:2]
		writer_1 = cv2.VideoWriter("Front_Camera_1.avi", fourcc, 20,(w * 2, h * 2), True)
		writer_2 = cv2.VideoWriter("Front_Camera_2.avi", fourcc, 20,(w * 2, h * 2), True)
		writer_3 = cv2.VideoWriter("Back_Camera.avi", fourcc, 20,(w * 2, h * 2), True)
		zeros = np.zeros((h, w), dtype="uint8")

	output = np.zeros((h * 2, w * 2, 3), dtype="uint8")
	output[0:h, 0:w] = frame_1
	output[0:h, w:w * 2] = frame_2
	output[h:h * 2, w:w * 2] = frame_3
	output[h:h * 2, 0:w] = frame_1

	cv2.imshow("Output", output)
	key = cv2.waitKey(1) & 0xFF

	# write the output frame to file
	writer_1.write(frame_1)
	writer_2.write(frame_2)
	writer_3.write(frame_3)


	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs_1.stop()
vs_2.stop()
vs_3.stop()
writer_1.release()
writer_2.release()
writer_3.release()