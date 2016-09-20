
import numpy as np
import matplotlib as plt
import cv2

from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976




def getColorBin(img, tl, br, numBins):
	mask = np.zeros(img.shape[:2], np.uint8)
	mask[tl[1]:br[1], tl[0]:br[0]] = 255

	debug = 0
	if debug:
		res = cv2.bitwise_and(img,img, mask = mask)
		cv2.imshow("mask",res)
		cv2.waitKey(0)

	hist = cv2.calcHist([img],[0],mask,[numBins],[0,256])

	bbin = np.argmax(hist)

	hist = cv2.calcHist([img],[1],mask,[numBins],[0,256])
	gbin = np.argmax(hist)

	hist = cv2.calcHist([img],[2],mask,[numBins],[0,256])
	rbin = np.argmax(hist)

	binNum = (bbin, gbin, rbin)
	if debug:
		print binNum

	return binNum

def lookupBin(binNum, numBins):
	c = (256 / numBins)
	return (c * binNum[0], c * binNum[1], c * binNum[2])


def colorDiff(color1, color2):
	return delta_e_cie1976(color1, color2)