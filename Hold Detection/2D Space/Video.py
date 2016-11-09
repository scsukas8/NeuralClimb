# Video capture example

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
from holdDetector import findHolds, findColors, plotColors


# Starting path
path = 'C:/Users/SeanC/Documents/GitHub/NeuralClimb/Hold Detection/2D Space/Test1-converted.avi'

# Open capture
cap = cv2.VideoCapture(path)

# Find dimensions of capture for output video
ret, frame = cap.read()
y,x,ch = frame.shape
outShape = (0,0)
if x > y:
    axis = 0
    y *= 2
else:
    axis = 1
    x *= 2
shape = (x,y)

# Open VideoWriter object
#codec = cv2.cv.CV_FOURCC('Y','V','1','2')
out = cv2.VideoWriter(path[:-4] + '-out.avi',-1, 30.0, shape,True)



while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Find keypoints
    keypoints, hulls = findHolds(frame)


    frameWithKeypoints = cv2.drawKeypoints(frame,keypoints,-1,[0,0,255])
    cv2.drawContours(frame,hulls,-1,[0,0,255])
    results = np.concatenate((frame, frameWithKeypoints), axis=axis)

    # Write image to video out
    out.write(results)  

    cv2.imshow('frame',results)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    



# When everything done, release the capture
out.release()
cap.release()
cv2.destroyAllWindows()
