import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
from holdDetector import findHolds, findColors, plotColors, buildDetector

import os.path
import time


i = 0
directory = "C:/Users/SeanC/Documents/GitHub/NeuralClimb/Hold Detection/2D Space/webcam/"
abspath = os.path.abspath(directory)

while (os.path.exists(abspath)):
    i+=1
    relpath = "Live" + "%04d" % i +".avi"
    path = directory + relpath
    abspath =  os.path.abspath(path)

cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
out = cv2.VideoWriter("webcam\\"+relpath,-1, 15.0, (640*2, 960/2),True)
detector = buildDetector()

while (True):

    retval, frame = cap.read()
    if retval == False:
        break

    #Find keypoints
    keypoints, _ = findHolds(frame,detector)

    #colors = findColors(frame,keypoints)

    frameWithKeypoints = cv2.drawKeypoints(frame,keypoints,-1,[0,0,255])
    results = np.concatenate((frame, frameWithKeypoints), axis=1)
    
    out.write(results)

    cv2.imshow('frame',results)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()