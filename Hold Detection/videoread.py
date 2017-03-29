import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
from holdDetector import findHolds, findColors, plotColors, buildDetector

import os.path
import time
#cap = cv2.VideoCapture(0)
#path = "C:/Users/SeanC/Documents/GitHub/NeuralClimb/Hold Detection/2D Space/results.avi"

#abspath =  os.path.abspath(path)
#cap = cv2.VideoCapture(abspath)

i = 0
detector = buildDetector()


# Define the codec and create VideoWriter object
out = cv2.VideoWriter('results.avi',-1, 15.0, (568,640),True)

while (True):
    i+=1

    file_path = "frames_" + "%04d" % i + ".png"
    print file_path
    frame = cv2.imread(file_path,1)
    if frame == None:
        break

 

    #Find keypoints
    keypoints, _ = findHolds(frame,detector)

    #colors = findColors(frame,keypoints)

    frameWithKeypoints = cv2.drawKeypoints(frame,keypoints,-1,[0,0,255])
    results = np.concatenate((frame, frameWithKeypoints), axis=0)
    
    print results.shape

    out.write(results)

    cv2.imshow('frame',results)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cap.release()
out.release()
cv2.destroyAllWindows()