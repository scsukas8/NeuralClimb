"""Example"""

import holdDetector as hd

#Open dialog to select image
img = hd.openImage()

# Finds each hold. Returns keypoints for each hold
# and the points that define the contours of each hold
holds, contours = hd.findHolds(img)


#Finds a color associated with each keypoint
colors = hd.findColors(img,holds)

#Draws keypoints onto image and plots colors in 3D space
hd.draw(img,holds)
hd.plotColors(colors)


