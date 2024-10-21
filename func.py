import cv2 as cv
import numpy as np

# this function return the interval of color pixel we want to detect

def get(color):
    c=np.uint8([[color]])  # enter bgr valur you want to convert to hsv
    hsv=cv.cvtColor(c,cv.COLOR_BGR2HSV)

    lower=hsv[0][0][0]-10,100,100
    upper=hsv[0][0][0]+10,255,255

    lower=np.array(lower,dtype=np.uint8)
    upper=np.array(upper,dtype=np.uint8)
    return lower,upper