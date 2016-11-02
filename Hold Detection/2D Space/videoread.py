import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
from holdDetector import findHolds, findColors, plotColors, buildDetector

import os.path
import time
#cap = cv2.VideoCapture(0)
path = "C:/Users/SeanC/Documents/GitHub/NeuralClimb/Hold Detection/2D Space/StopMoti2001.mpeg"

abspath =  os.path.abspath(path)
print os.path.exists(abspath)
print abspath
cap = cv2.VideoCapture(abspath)

print cap.isOpened()

i = 0
detector = buildDetector()


# Define the codec and create VideoWriter object
out = cv2.VideoWriter('results.avi',-1, 15.0, (568,320),True)

while not (cap.isOpened()):
    i+=1

    file_path = "frames_" + "%04d" % i + ".png"
    print file_path
    frame = cv2.imread(file_path,1)
    if frame == None:
        break



    #Find keypoints
    keypoints, _ = findHolds(frame,detector)

    #colors = findColors(frame,keypoints)

    frameWithKeypoints = cv2.drawKeypoints(frame,keypoints,-1,[255,0,0])
    results = np.concatenate((frame, frameWithKeypoints), axis=0)
    
    out.write(frameWithKeypoints)

    cv2.imshow('frame',results)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()