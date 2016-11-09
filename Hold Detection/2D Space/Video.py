# Video capture example

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
from holdDetector import findHolds, findColors, plotColors



path = 'C:/Users/SeanC/Documents/GitHub/NeuralClimb/Hold Detection/2D Space/Test3-converted.avi'
cap = cv2.VideoCapture(path)

out = cv2.VideoWriter(path[:-4] + '-out.avi',-1, 30.0, (568,640),True)


while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    #Find keypoints
    keypoints, hulls = findHolds(frame)


    


    frameWithKeypoints = cv2.drawKeypoints(frame,keypoints,-1,[0,0,255])
    #cv2.drawContours(frame,hulls,-1,[255,0,0])
    results = np.concatenate((frame, frameWithKeypoints), axis=0)

 

    # Write image to video out
    out.write(results)  

    cv2.imshow('frame',results)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    



# When everything done, release the capture
out.release()
cap.release()
cv2.destroyAllWindows()