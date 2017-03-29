# Video capture example

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
from holdDetector import findHolds, findColors, plotColors
cap = cv2.VideoCapture('C:/Users/SeanC/Documents/GitHub/NeuralClimb/Hold Detection/2D Space/TestVideo-clipped-converted.avi')


ret, frame = cap.read()
r,c,ch = frame.shape
mask = np.zeros((c,r))



while(cap.isOpened()):
    mask2 = np.zeros((c,r))

    mask3 = np.zeros((c,r))


    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    #Find keypoints
    keypoints, _ = findHolds(frame)

    for key in keypoints:
        #mask[key.pt] =+25
        cv2.circle(mask2,(int(key.pt[1]),int(key.pt[0])),5,2,-1)
    
    mask += 
    mask[mask > 0] = mask[mask > 0] - 1

    mask3 = mask2 > 200

    """
    for r,row in enumerate(mask):
        for c,col in enumerate(row):
            if mask[r,c] > 1:
                cv2.circle(frame,(r,c),10,[0,0,255],-1)
    """

    #im_with_keypoints = cv2.drawKeypoints(frame,keypoints,-1,[255,0,0])
    
    frame[:,:,2] = frame[:,:,2] + mask.T

    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()