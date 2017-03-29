#Utility file with convenient functions

import matplotlib as plt
import cv2
from PIL import Image
import Tkinter as tk, Tkconstants, tkFileDialog


def openFile():
    root = tk.Tk()
    root.withdraw()
    file_path = tkFileDialog.askopenfilename()
    return file_path

def openImage(file_path = None):
    # If no file path given, open dialog
    if file_path is None:
        file_path = openFile()
    
    # If stil no file path chosen, quit
    if file_path == None:
        return None

    image = cv2.imread(file_path,1)
    return image

def grab_from_webcam():
    # Start webcam capture
    cap = cv2.VideoCapture(0)

    # Pause for webcam to adjust
    time.sleep(1)

    # Grabs a frame from the capture
    retval, frame = cap.read()

    # Release webcam
    cap.release()

    return (retval, frame)

def grab_from_file(file_path = None):
    frame = openImage(file_path)
    retval = not frame is None

    return (retval, frame)

def resize(image, y = 0, x = 0):
    if y == 0:
        return image
    if x == 0:
        r, c, _ = image.shape
        x = y * c / r;
    image = cv2.resize(image, (y,x))
    return image

def showImage(image, title = "Image"):
    if image is None:
        "Warning: Image is None"
        return
    cv2.imshow(title,image)
    cv2.waitKey(0)
