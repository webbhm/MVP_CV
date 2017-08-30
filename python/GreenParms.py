import cv2
import numpy as np
import copy
import os
import findPlantUtil as fpu

def nothing(x):
    pass

def findPlant(src, lower, upper):
    #warp=fpu.transform(src)
    mask=fpu.getMask(src, lower, upper)
    edge=fpu.getEdges(mask)
    cv2.imshow('Edge', edge)
    ellipse=fpu.getContours(edge, src)
    cv2.imshow('Ellipse', ellipse)
    cv2.waitKey(5)
    return ellipse

lower = np.array([33,39,111])
upper = np.array([64,255,255])

# Create a black image, a window
u_img = np.zeros((300,512,3), np.uint8)
l_img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('Upper')
cv2.namedWindow('Lower')

# create trackbars for color change
# Upper
cv2.createTrackbar('R','Upper', upper[1], 255,nothing)
cv2.createTrackbar('G','Upper',upper[2],255,nothing)
cv2.createTrackbar('B','Upper',upper[0],255,nothing)

# Lower range
cv2.createTrackbar('R_min','Lower',lower[1],255, nothing)
cv2.createTrackbar('G_min','Lower',lower[2],255, nothing)
cv2.createTrackbar('B_min','Lower',lower[0],255, nothing)

#Get the pic
#pic = '/home/pi/webcam/2017-08-22_1701.jpg'
pic='/home/pi/webcam/2017-08-03_1401.jpg'
src = cv2.imread(pic)

while(1):
    findPlant(src, lower, upper)
    
    cv2.imshow('Upper',u_img)
    cv2.imshow('Lower',l_img)
#    plant=findPlant(src, lower, upper)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    upper[1] = cv2.getTrackbarPos('R','Upper')
    upper[2] = cv2.getTrackbarPos('G','Upper')
    upper[0] = cv2.getTrackbarPos('B','Upper')

    lower[1] = cv2.getTrackbarPos('R_min','Lower')
    lower[2] = cv2.getTrackbarPos('G_min','Lower')
    lower[0]= cv2.getTrackbarPos('B_min', 'Lower')
    print(upper)
    print(lower)

    u_img[:] = upper
    l_img[:] = lower
   
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
