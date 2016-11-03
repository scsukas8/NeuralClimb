#Utility file used for Neural Climb Project

import matplotlib as plt
import cv2
from PIL import Image
import Tkinter as tk, Tkconstants, tkFileDialog


def openFile():
	root = tk.Tk()
	root.withdraw()
	file_path = tkFileDialog.askopenfilename()
	return file_path

def showim(title, im):
	cv2.imshow(title,im )
	cv2.waitKey(0)
