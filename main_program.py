import threading
from threading import Thread
import cv2
import numpy as np
from multiprocessing import Process

def camera_1():
	cap_1 = cv2.VideoCapture(1)

	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out_1 = cv2.VideoWriter('Front_Camera_1.avi',fourcc, 20.0, (640,480))

	while(cap_1.isOpened()):
		ret, frame_1 = cap_1.read()
		out_1.write(frame_1)
		cv2.imshow('frame',frame_1)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap_1.release()
	out_1.release()
	cv2.destroyAllWindows()

def camera_2():
	cap_2 = cv2.VideoCapture(1)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out_2 = cv2.VideoWriter('Front_Camera_2.avi',fourcc, 20.0, (640,480))

	while(cap_2.isOpened()):
		ret, frame_2 = cap_2.read()
		out_2.write(frame_2)
		cv2.imshow('frame',frame_2)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap_2.release()
	out_2.release()
	cv2.destroyAllWindows()

def camera_3():
	cap_3 = cv2.VideoCapture(1)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out_3 = cv2.VideoWriter('Back_Camera.avi',fourcc, 20.0, (640,480))
	while(cap_3.isOpened()):
		ret, frame_3 = cap_3.read()
		out_3.write(frame_3)
		cv2.imshow('frame',frame_3)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap_3.release()
	out_3.release()
	cv2.destroyAllWindows()

def runInParallel(*fns):
	proc = []
 	for fn in fns:
		p = Process(target=fn)
		p.start()
		proc.append(p)
	for p in proc:
		p.join()

if __name__ == '__main__':

	# MutltiThreading
	# Thread(target = camera_1).start()
	# Thread(target = camera_2).start()
	# Thread(target = camera_3).start()

	# MultiProcessing
	# Process(target = camera_1).start()
	# Process(target = camera_2).start()
	# Process(target = camera_3).start()\

	# Running functions in parallel
	runInParallel(camera_1, camera_2, camera_3)