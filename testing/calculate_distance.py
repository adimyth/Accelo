import numpy as np
import cv2
 
knownWidth = 11.6
# knownDistance = 20
focalLength = 0.173228
distance = []
difference_in_distances = []

# Calculating the focal length of the camera
# image = cv2.imread("paper.jpg")
# marker = find_marker(image)
# focalLength = (marker[1][0] * knownDistance) / knownWidth

def strictly_decreasing(L):
    return all(x>y for x, y in zip(L, L[1:]))

def find_marker(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)

	_, cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	c = max(cnts, key = cv2.contourArea)
	return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
	return (knownWidth * focalLength) / perWidth

# 0 for primary source and 1 for secondary source
cap = cv2.VideoCapture(1)
while (True and cap.isOpened()):
	_, image = cap.read()
	marker = find_marker(image)
	inches = distance_to_camera(knownWidth, focalLength, marker[1][0]*0.0002145)
	# print(marker[1][0])
	print(inches)

	# Code to calculate the reducing differences in distance from the object
	distance.append(inches)
	difference_in_distances = [x - distance[i - 1] for i, x in enumerate(distance)][1:]
	# if strictly_decreasing(difference_in_distances):
	# 	print("Difference is reducing continously")
	# else :
	# 	print("Chances of collision is low")
	# If buffer size exceeds, then flush all the previous calculations	
	if len(distance) == 10:
		distance = []
		difference_in_distances = []

	box = np.int0(cv2.boxPoints(marker))
	cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
	cv2.putText(image, "%.2fft" % (inches / 12),(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
	cv2.imshow("image", image)
	if cv2.waitKey(1)&0xFF == ord('q'):
		break
cv2.destroyAllWindows()