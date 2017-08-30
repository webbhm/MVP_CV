# Test code working on a single image

import numpy as np
import cv2
import findPlantUtil as fpu

# define upper and lower range of green color in HSV
lower = np.array([33,39,111])
upper = np.array([64,255,255])

# Custom transformation points
pts_in=np.float32([[461,0][1052,0][358,720][1189,720]])
pts_out=np.float32([[0,0][831,0][0,720][831,720]])

pic = '/home/pi/webcam/2017-08-22_1701.jpg'
#Read the file into an array
src = cv2.imread(pic)
warp=fpu.transform(src, pts_in, pts_out)
#cv2.imshow('Warp', warp)

mask=fpu.getMask(warp, lower, upper)
cv2.imshow('Mask',mask)
cv2.waitKey(2)

res = cv2.bitwise_and(warp,warp, mask= mask)

edge=fpu.getEdges(mask)
cv2.imshow('Edges', edge)
cv2.waitKey(2)

ellipse=fpu.getContours(edge, warp)
print(type(ellipse))

cv2.imshow('Elipse', ellipse)
#cv2.imwrite('/home/pi/MVP/Pictures/Ellipse.png', src2)

# Wat for the escape key to be pressed to end - does not work with Python IDE
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
