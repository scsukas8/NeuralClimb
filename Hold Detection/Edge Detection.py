import cv2
import numpy as np
import matplotlib.pyplot as plt
from util import openFile

file_path = openFile()
img = cv2.imread(file_path,0)

#Image is resized to a resonable size to fit screen and
#speed up processing speed.
c = 1000.0/img.shape[0]
x = int(img.shape[0] * c)
y = int(img.shape[1] * c)
img = cv2.resize(img, (y,x))


edges = cv2.Canny(img,150,200)

plt.subplot(121)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image')
plt.xticks([])
plt.yticks([])

plt.show()