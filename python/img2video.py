'''
tk-img2video -ext png -o output.mp4
'''

#!/usr/local/bin/python3

import cv2
import argparse
import os

# Arguments
dir_path = '/home/pi/webcam/Group1/'
ext = 'png'
output = '/home/pi/webcam/Group1/out.avi'

images = []
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)
#        print(f)

images.sort()
#print(images)
# Determine the width and height from the first image
image_path = os.path.join(dir_path, images[0])
#print(image_path)
frame = cv2.imread(image_path)
cv2.imshow('video',frame)
height, width, channels = frame.shape

# Define the codec and create VideoWriter object
# Only works with avi, others don't work at this time
fourcc = cv2.cv.CV_FOURCC(*'xvid')
out = cv2.VideoWriter(output, fourcc, 1.5, (width, height))

for image in images:

    image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image_path)

    out.write(frame) # Write out frame to video

#    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

# Release everything if job is finished
out.release()
#cv2.destroyAllWindows()

print("The output video is {}".format(output))
