import numpy as np
import cv2
import os.path
from util import openFile


file_path = openFile()
cap = cv2.VideoCapture(file_path)

print cap.isOpened()
i = 0

while not (cap.isOpened()):
    i+=1

    file_path = "frames_" + "%04d" % i + ".png"
    print file_path
    frame = cv2.imread(file_path,1)
    if frame == None:
        break

    out.write(results)

    cv2.imshow('frame',results)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()