import cv2
import numpy as np
import cv2.aruco as aruco

# Aruco parameters
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
parameters = aruco.DetectorParameters_create()

img = cv2.imread('img0107.jpg')
resized = cv2.resize(img, (1080, 720), interpolation=cv2.INTER_AREA)
#cv2.imshow("Img", resized)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
offset = 28
ypos = int(corners[0][0][2][1]) + offset
mask = np.zeros((resized.shape[0], resized.shape[1], 3), np.uint8)
mask[ypos:] = 255
croped = cv2.bitwise_and(resized, mask)
cv2.imshow("Cropped", croped)
cv2.waitKey(0)
cv2.destroyAllWindows()
