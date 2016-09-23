import cv2
import numpy as np
import matplotlib.pyplot as plt
from util import openFile, showim


def buildDetector():
	# Setup SimpleBlobDetector parameters.
	params = cv2.SimpleBlobDetector_Params()

	# Change thresholds
	params.minThreshold = 0
	params.maxThreshold = 255


	# Filter by Area.
	params.filterByArea = True
	params.minArea = 80

	# Filter by Circularity
	params.filterByCircularity = True
	params.minCircularity = 0.01

	# Filter by Convexity
	params.filterByConvexity = True
	params.minConvexity = 0.01
	    
	# Filter by Inertia
	params.filterByInertia = True
	params.minInertiaRatio = 0.01

	# Create a detector with the parameters
	ver = (cv2.__version__).split('.')
	if int(ver[0]) < 3 :
		detector = cv2.SimpleBlobDetector(params)
	else : 
		detector = cv2.SimpleBlobDetector_create(params)

	return detector


file_path = openFile()
img = cv2.imread(file_path,1)
#img = cv2.imread('Image3.jpg',1)

#Image is resized to a resonable size to fit screen and
#speed up processing speed.
c = 1000.0/img.shape[0]
x = int(img.shape[0] * c)
y = int(img.shape[1] * c)

img = cv2.resize(img, (y,x))



edges = cv2.Canny(img,250,300)


contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

mask = np.zeros(img.shape,np.uint8)

cnt = [cnt for cnt in contours if cv2.contourArea(cnt) > 10]


hulls = map(cv2.convexHull,cnt)



cv2.drawContours(mask,hulls,-1,[255,0,0])



#plt.imshow(imgray)
#plt.title('Edge with Contours')
showim('Edge with Contours',mask)


# Set up the detector with default parameters.
detector = buildDetector()


keypoints = detector.detect(mask)
color = (0,0,255)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(mask, keypoints, np.array([]), color, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

showim('Contours with keypoints',im_with_keypoints)
