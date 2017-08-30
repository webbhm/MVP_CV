# Batch process a directory of images

import numpy as np
import cv2
import findPlantUtil as fpu

def findPlants(file, lower, upper, out_dir, pts_in, pts_out ):

    src = cv2.imread(file)
    warp=fpu.transform(src, pts_in, pts_out)
    mask=fpu.getMask(warp, lower, upper)
    edge=fpu.getEdges(mask)
    ellipse=fpu.getContours(edge, warp)
    return ellipse

# define upper and lower range of green color in HSV
lower = np.array([33,39,111])
upper = np.array([64,255,255])

# Custom transformation points
pts_in=np.float32([[461,0][1052,0][358,720][1189,720]])
pts_out=np.float32([[0,0][831,0][0,720][831,720]])

p='.'
s='/'
path='/home/pi/webcam/Group1/'
out_dir='/home/pi/webcam/Group1/'

for file in os.listdir(path):
    if file.endswith('.jpg'):
        print(path + file)
        plant=findPlants(path + file, out_dir, pts_in, pts_out)
        #Save the file
        x=file.split(s)
        f=x[-1].split(p)
        new_file=out_dir + f[-2] + '.png'
        cv2.imwrite(new_file, plant)
