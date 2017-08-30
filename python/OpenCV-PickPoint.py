import cv2
import numpy as np

pic = '/home/pi/webcam/2017-08-22_1701.jpg'
ix,iy = -1,-1
font = cv2.FONT_HERSHEY_SIMPLEX

# mouse callback function
def print_text(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_MOUSEMOVE:
        img=np.copy(img_hld)
        cv2.putText(img,str([x,y]),(10,500), font, 4,(255,255,255),2,cv2.CV_AA)
        cv2.imshow('image', img)

img_hld = cv2.imread(pic)
img = np.copy(img_hld)
cv2.namedWindow('image')
cv2.setMouseCallback('image',print_text)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while(1):
   # cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cv2.waitKey(2)
