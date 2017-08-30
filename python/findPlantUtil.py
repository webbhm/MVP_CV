# Routines to find plants and draw ellipse

import numpy as np
import cv2
import copy

def transform(src, pts_in, pts_out):

    # Prepare the image for work, straighten and clip
    #gimg=cv2.imread(pic, cv2.IMREAD_GRAYSCALE)
    '''
    # Perspective transform to straighten
    top=0
    left=0
    bottom=720
    # Use OpenCV-PickPoints to find the points
    # Source top points
    source_tl_x=461
    source_tl_y=top  #Always measure from the top edge
    source_tr_x=1052
    source_tr_y=top
    # Source bottom points
    source_bl_x=358
    source_bl_y=bottom
    source_br_x=1189
    source_br_y=bottom

    # Calculate width of output image
    width=source_br_x - source_bl_x

    # Build input points
    pts_in=np.float32([[source_tl_x, source_tl_y],[source_tr_x, source_tr_y],[source_bl_x,source_bl_y],[source_br_x,source_br_y]])
    # Define output points (clip to left edge
    pts_out=np.float32([[top, left],[width,left],[top,bottom],[width,bottom]])
    print(pts_in)
    print(pts_out)
    '''
    # Perform transformation warp
    M=cv2.getPerspectiveTransform(pts_in, pts_out)
    #print(M)
    warp=cv2.warpPerspective(src, M,(724,720))
    return warp

def getMask(img, lower, upper):

    #Begin finding of plants
    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    print("image type: ", type(hsv))

    # Threshold the HSV image to get only green colors and create mask of greens
    mask = cv2.inRange(hsv, lower, upper)

    # erode and dialate the image to remove artifacts
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(erosion, kernel, iterations=5)
    erosion2 = cv2.erode(dilation, kernel, iterations = 3)

    # Create a test image showing the green through the mask
    # Not actually used, but interesting to play with
    return erosion2

#bgr=cv2.cvtColor(erosion2, cv2.COLOR_HSV2BGR)
#gr=cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)


def getEdges(img):

    BLACK=[0, 0, 0]
    #Border the image so edges run around ends
    bdr=cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLACK)

    # Detect the edges of the plants
    edges=cv2.Canny(bdr, 100, 200)
    print(edges.shape)
    return edges

def getContours(img, display):
    # Build contours of the plants from the edges
    # Only get top level (external) contours
    contours,hierarchy= cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Copy the image, otherwise it would be overwritten and no longer available
    out=copy.copy(display)
    # Walk all the contours
    x=0 # Counter for display
    for i in contours:
        x=x+1
        # Create and draw the elipses - this is the final output image
        if cv2.contourArea(i) > 5:
            ellipse = cv2.fitEllipse(i)
            cv2.ellipse(out, ellipse,(0,0,0),2)
        else:
            print("Too small of area for evaluation", x, cv2.contourArea(i))
        
        # The area could be used to calculate phenotype info
#        print("Contour: ", x, "Area: ", cv2.contourArea(i))
    return out
