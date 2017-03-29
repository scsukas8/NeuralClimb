import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
from holdDetector import findHolds, findColors, plotColors, buildDetector

import os.path
import time

# Determine output path of video
i = 0
directory = "C:/Users/SeanC/Documents/GitHub/NeuralClimb/Hold Detection/2D Space/webcam/"
abspath = os.path.abspath(directory)

# Increment video number to not overwrite old files.
while (os.path.exists(abspath)):
    i+=1
    relpath = "Live" + "%04d" % i +".avi"
    path = directory + relpath
    abspath =  os.path.abspath(path)

# Start webcam capture
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
out = cv2.VideoWriter("webcam\\"+relpath,-1, 15.0, (640*2, 960/2),True)
detector = buildDetector()


while (cap.isOpened()):
    start = time.time()

    # Pull in frame from webcam
    retval, frame = cap.read()
    if retval == False:
        break

    #Find keypoints
    keypoints, _ = findHolds(frame,detector)

    #Draw Keypoints onto frame
    frameWithKeypoints = cv2.drawKeypoints(frame,keypoints,-1,[0,0,255])

    #Display frame with keypoint frame side by side.
    results = np.concatenate((frame, frameWithKeypoints), axis=1)
    
    # Write image to video out
    out.write(results)

    #Display for user.
    cv2.imshow('frame',results)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    end = time.time()
    print(end - start)

cap.release()
out.release()
cv2.destroyAllWindows()