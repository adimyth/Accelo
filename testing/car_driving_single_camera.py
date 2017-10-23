# this program will be able to detect blue and red colored boxes & trianges
import cv2
import imutils
import numpy as np

# obstacles dimensions
box_height = 
box_width =
triangle_height = 
triangle_width = 
focalLength = 0.173228

# calculating the aspect ratio of the objects
aspect_ratio_box = box_width/ float(box_height)
aspect_ratio_triangle = triangle_width/ float(triangle_height)

# tolerance for the aspect_ratio object detected in the image
tolerance_box = 
tolerance_triangle = 
aspect_ratio_box_lower_bound = aspect_ratio_box - tolerance_box
aspect_ratio_box_upper_bound = aspect_ratio_box + tolerance_box
aspect_ratio_triangle_lower_bound = aspect_ratio_triangle - tolerance_triangle
aspect_ratio_triangle_upper_bound = aspect_ratio_triangle + tolerance_triangle

cap = cv2.VideoCapture(0)
# color ranges for blue and green color
blue_lower  = (110,100,100)
blue_upper  = (130,255,255)
green_lower = (50,100,100)
green_upper = (70,255,255)

# lists to store the contours coordinates
arr_blue_quad = []
arr_blue_triangle = []
arr_green_quad = []
arr_green_triangle = []

# function to calculate the distance of object from camera
def distance_to_camera(knownWidth, focalLength, perWidth):
	return (knownWidth * focalLength) / perWidth

while True and cap.isOpened():
	ret, frame = cap.read()
	frame = imutils.resize(frame, width=600)
	blur = cv2.GaussianBlur(frame, (11,11), 0)
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

	# mask_blue to identify the blue color
	mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)
	mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_NONE, None)

	# mask_green to identify the green color
	mask_green = cv2.inRange(hsv, green_lower, green_upper)
	mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_NONE, None)

	# to handle blue colored obstacles
	cnts_blue = cv2.findContours(mask_blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	if len(cnts_blue) > 0:
		for cnt in cnts_blue:
			approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True), True)
			# check for quadrilaterals and cones
			if len(approx) == 4:
				arr_blue_quad.append(cnt)
			elif len(approx) == 3:
				arr_blue_triangle.append(cnt)

		for cnt in arr_blue_quad:
			x,y,w,h = cv2.boundingRect(cnt)
			aspect_ratio = w/ float(h)
			if aspect_ratio <= aspect_ratio_box_upper_bound and >= aspect_ratio_box_lower_bound:
				cv2.putText(frame, 'Box', (x,y), (0,255,0))
				distance = distance_to_camera(box_width, focalLength, w)
				if distance < :
					cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)					
				else:
					cv2.rectangle(frame, (x,y), (x+w,y+h), (255,99,71), 2)				

		for cnt in arr_blue_triangle:
			x,y,w,h = cv2.boundingRect(cnt)
			aspect_ratio = w/ float(h)
			if aspect_ratio <= aspect_ratio_triangle_upper_bound and >= aspect_ratio_triangle_lower_bound:
				cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
				cv2.putText(frame, 'Triangle', (x,y), (0,255,0), 2)

		cv2.imshow('Obstacle Tracking', frame)
		key = cv2.waitKey(0)
		if key == ord('q'):
			break

	# to handle green colored obstacles
	cnts_green = cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	if len(cnts_green) > 0:
		for cnt in cnts_green:
			approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True), True)
			# check for quadrilaterals and triangles
			if len(approx) == 4:
				arr_green_quad.append(cnt)
			elif len(approx) == 3:
				arr_green_triangle.append(cnt)

		for cnt in arr_green_quad:
			x,y,w,h = cv2.boundingRect(cnt)
			aspect_ratio = w/ float(h)
			if aspect_ratio <= aspect_ratio_box_upper_bound and >= aspect_ratio_box_lower_bound:
				cv2.putText(frame, 'Box', (x,y), (0,0,255), 2)
				distance = distance_to_camera(box_width, focalLength, w)
				if distance < :
					cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
				else:
					cv2.rectangle(frame, (x,y), (x+w,y+h), (255,99,71), 2)

		for cnt in arr_green_triangle:
			x,y,w,h = cv2.boundingRect(cnt)
			aspect_ratio = w/ float(h)
			if aspect_ratio <= aspect_ratio_triangle_upper_bound and >= aspect_ratio_triangle_lower_bound:
				cv2.putText(frame, 'Triangle', (x,y), (0,0,255), 2)
				distance = distance_to_camera(triangle_width, focalLength, w)
				if distance < :
					cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
				else:
					cv2.rectangle(frame, (x,y), (x+w,y+h), (255,99,71), 2)		

		cv2.imshow('Obstacle Tracking', frame)
		key = cv2.waitKey(0)
		if key == ord('q'):
			break

cap.release()
cv2.destroyAllWindows()