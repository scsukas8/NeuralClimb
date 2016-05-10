import numpy as np
import matplotlib as plt
import cv2
from PIL import Image


def buildDetector():
	# Setup SimpleBlobDetector parameters.
	params = cv2.SimpleBlobDetector_Params()

	# Change thresholds
	params.minThreshold = 0
	params.maxThreshold = 255


	# Filter by Area.
	params.filterByArea = True
	params.minArea = 70

	# Filter by Circularity
	params.filterByCircularity = False
	params.minCircularity = 0.1

	# Filter by Convexity
	params.filterByConvexity = False
	params.minConvexity = 0.1
	    
	# Filter by Inertia
	params.filterByInertia = False
	params.minInertiaRatio = 0.01

	# Create a detector with the parameters
	ver = (cv2.__version__).split('.')
	if int(ver[0]) < 3 :
		detector = cv2.SimpleBlobDetector(params)
	else : 
		detector = cv2.SimpleBlobDetector_create(params)

	return detector

def getColorBin(img, tl, br, numBins):
	mask = np.zeros(img.shape[:2], np.uint8)
	mask[tl[1]:br[1], tl[0]:br[0]] = 255


	#res = cv2.bitwise_and(img,img, mask = mask)
	#cv2.imshow("mask",res)
	#cv2.waitKey(0)

	hist = cv2.calcHist([img],[0],mask,[numBins],[0,256])

	bbin = np.argmax(hist)

	hist = cv2.calcHist([img],[1],mask,[numBins],[0,256])
	gbin = np.argmax(hist)

	hist = cv2.calcHist([img],[2],mask,[numBins],[0,256])
	rbin = np.argmax(hist)

	binNum = (bbin, gbin, rbin)
	print binNum

	return binNum

def lookupBin(binNum, numBins):
	c = (256 / numBins)
	return (c * binNum[0], c * binNum[1], c * binNum[2])


	

im = cv2.imread("sample4.jpg")
hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

count = 0
# Set up the detector with default parameters.
detector = buildDetector()

LowH = 79
LowS = 0
LowV = 0
HighH = 110
HighS = 138
HighV = 255

def onChange(e):
	return e

cv2.namedWindow("Filter Settings", cv2.WINDOW_NORMAL) 

cv2.createTrackbar("Low Hue", "Filter Settings", LowH, 179, onChange)
cv2.createTrackbar("High Hue", "Filter Settings", HighH, 179, onChange)

cv2.createTrackbar("Low Sat", "Filter Settings", LowS, 255, onChange)
cv2.createTrackbar("High Sat", "Filter Settings", HighS, 255, onChange)

cv2.createTrackbar("Low Value", "Filter Settings", LowV, 255, onChange)
cv2.createTrackbar("High Value", "Filter Settings", HighV, 255, onChange)

img = cv2.medianBlur(hsv[:,:,0],5)

imfilt = cv2.adaptiveThreshold(img,255, \
	cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2)

keypoints = detector.detect(imfilt)
color = (0,0,255)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(imfilt, keypoints, np.array([]), color, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
#cv2.imshow("Keypoints", im_with_keypoints)


while 1:

	LowH = cv2.getTrackbarPos("Low Hue", "Filter Settings")
	LowS = cv2.getTrackbarPos("Low Sat", "Filter Settings")
	LowV = cv2.getTrackbarPos("Low Value", "Filter Settings")
	HighH = cv2.getTrackbarPos("High Hue", "Filter Settings")
	HighS = cv2.getTrackbarPos("High Sat", "Filter Settings")
	HighV = cv2.getTrackbarPos("High Value", "Filter Settings")

	filtered = cv2.inRange(hsv,(LowH,LowS,LowV),(HighH,HighS,HighV))
	filtered = cv2.medianBlur(filtered,11)

	# Detect blobs.
	keypoints = detector.detect(filtered)
	cv2.imshow("Filter", filtered)
	color = (0,0,255)

	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
	im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), color, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

	# Show keypoints
	cv2.imshow("Keypoints", im_with_keypoints)
	#cv2.imshow("Hue Layer",hsv[:,:,0])


	if (cv2.waitKey(30) == 27):
		break

#cv2_im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
#pil_im = Image.fromarray(cv2_im)

numBins = 4
for key in keypoints:
	x = int(key.pt[0])
	y = int(key.pt[1])
	print 
	size = 20
	size2 = size * 2
	br = (x + size, y + size)	
	tl = (x - size, y - size)

	br2 = (x + size2, y + size2)	
	tl2 = (x - size2, y - size2)
	
	colorBin = getColorBin(im,tl,br,numBins)

	color = lookupBin(colorBin,numBins)
	
	cv2.rectangle(im, tl2, br2, color)

cv2.imshow("Detection",im)
cv2.waitKey(0)
