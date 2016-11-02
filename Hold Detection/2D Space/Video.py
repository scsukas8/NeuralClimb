# Video capture example

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
from holdDetector import findHolds, findColors, plotColors

cap = cv2.VideoCapture('C:/Users/SeanC/Documents/GitHub/NeuralClimb/Hold Detection/2D Space/drop.avi')



while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #Find keypoints
    keypoints, _ = findHolds(frame)

    colors = findColors(frame,keypoints)


    im_with_keypoints = cv2.drawKeypoints(frame,keypoints,-1,[255,0,0])
    cv2.imshow('frame',im_with_keypoints)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()