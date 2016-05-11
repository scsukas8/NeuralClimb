import cv2
import numpy as np
import matplotlib.pyplot as plt
from util import openFile
from color import lookupBin, getColorBin

file_path = openFile()
im = cv2.imread(file_path)

#Image is resized to a resonable size to fit screen and
#speed up processing speed.
c = 1000.0/im.shape[0]
x = int(im.shape[0] * c)
y = int(im.shape[1] * c)
im = cv2.resize(im, (y,x))


imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

numBins = 4
imhsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)

for cnt in contours:
	area = cv2.contourArea(cnt)
	if area > 10 and area < 10000:	
		#x,y,w,h = cv2.boundingRect(cnt)

		#colorBin = getColorBin(im, (x, y), (x + w, y + h), numBins)
		#color = lookupBin(colorBin, numBins)

		mask = np.zeros(imgray.shape,np.uint8)
		cv2.drawContours(mask,[cnt],0,255,-1)
		meanColor = cv2.mean(imhsv,mask = mask)


		meanColor = np.uint8([[[meanColor[0],
								meanColor[1],
						   	 	meanColor[2]]]])
		
		color = cv2.cvtColor(np.array(meanColor),cv2.COLOR_HSV2BGR)
		color = (int(color[0][0][0]),
				 int(color[0][0][1]),
				 int(color[0][0][2]))

		print cv2.mean(im,mask = mask)
		print color


		cv2.drawContours(im, [cnt], 0, color, -1)

cv2.imshow("contours",im)
cv2.waitKey(0)