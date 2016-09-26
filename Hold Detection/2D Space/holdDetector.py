import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from util import openFile, showim
import colorsys
from mpl_toolkits.mplot3d import Axes3D




def openImage():
    # Open Image
    file_path = openFile()
    img = cv2.imread(file_path,1)
    #img = cv2.imread('Image3.jpg',1)

    # Image can be resized to a resonable size to fit screen and
    # speed up processing.
    #c = 1000.0/img.shape[0]
    #x = int(img.shape[0] * c)
    #y = int(img.shape[1] * c)
    #img = cv2.resize(img, (y,x))



    return img

""" Object detection """

def buildDetector():
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 0
    params.maxThreshold = 255


    # Filter by Area.
    params.filterByArea = True
    params.minArea = 30

    # Filter by Circularity
    params.filterByCircularity = False
    params.minCircularity = 0.01

    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = 0.01
        
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


def findHolds(img):
    # Applying a median blur removes some small impurities that
    # could fool the detection algorithm. It also smooths out the
    # color of each hold to make it more uniform.
    blur = cv2.medianBlur(img,11)

    # Applys edge detection to find the borders between the hold and the wall
    # This should be modified to adapt to different settings.
    edges = cv2.Canny(blur,100,250)


    # Finds the contours of the image, without retaining the hierarchy
    contours, _ = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # Remove contours that are too small or have too few points.
    cnt = [cnt for cnt in contours if cv2.contourArea(cnt) > 10 and cnt.size > 5]

    # Applies convex hulls to each contour, ensuring each contour
    # is a closed polygon.
    hulls = map(cv2.convexHull,cnt)

    # Draws contours onto a blank canvas
    mask = np.zeros(img.shape,np.uint8)
    cv2.drawContours(mask,hulls,-1,[255,0,0])




    # Set up the detector with default parameters.
    detector = buildDetector()

    keypoints = detector.detect(mask)
    return keypoints



""" Color manipulations """

def getColorBin(img, tl, br):
    # Creates mask over image focus
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[tl[1]:br[1], tl[0]:br[0]] = 255

    # Effecively quantizes the image when the histogram is made.
    # Useful for grouping similar colors.
    binLen = 4
    numBins = 256 / binLen

    #Finds the most common color/in the histogram/for each color channel.
    binColor = map(
        lambda x: np.argmax(
        [cv2.calcHist([img],[x],mask,[numBins],[0,256])])
        ,[0,1,2])

    fullColor = map(lambda x: x * binLen, binColor)

    return fullColor 

def findColors(img,keypoints):

    #Shift colorspace to HLS
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)

    # Preallocate space for color array corresponding to keypoints
    colors = np.empty([len(keypoints),3])

    # Iterates through the keypoints and finds the most common
    # color at each keypoint.
    for i, key in enumerate(keypoints):
    	x = int(key.pt[0])
    	y = int(key.pt[1])

    	size = int(math.ceil(key.size)) 

        #Finds a rectangular window in which the keypoint fits
    	br = (x + size, y + size)	
    	tl = (x - size, y - size)

    	colors[i] = getColorBin(hsv,tl,br)
    
    return colors


""" Visualization """
def draw(img, keypoints):
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the 
    # size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]),
     (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    #OpenCV uses BGR format, so that'll need to be reversed for display
    im_with_keypoints = im_with_keypoints[...,::-1]

    # Display the resulting frame
    fig = plt.imshow(im_with_keypoints)
    plt.title("Image with Keypoints")




def plotColors(colors):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([], [], [], c=[0,0,0], marker='o')


    rs = []
    gs = []
    bs = []

    for color in colors:
        rs.append(color[0])
        gs.append(color[1])
        bs.append(color[2])


    ax.scatter(rs, gs, bs, c=colors/256.0, marker='o')

    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')

    ax.set_xlim(0,255)
    ax.set_ylim(0,255)
    ax.set_zlim(0,255)

    plt.title("Color Space of Keypoints")
    plt.show()
		


