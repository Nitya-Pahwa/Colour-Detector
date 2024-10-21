import cv2 as cv
from PIL import Image
from func import get
cap=cv.VideoCapture(0)
color=[0,255,255]  #yellow

# HSV -  hue saturation value
# hue is respnsible for color
# we will be defining an interval for any color detection
# give 2 values and ask proram to give all color pixels in this range
while(True):
    ret,frame=cap.read()
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)  # converting image from bgr to hsv

    lower,upper=get(color)
    
    mask=cv.inRange(hsv,lower,upper) # give location of all pixels we want to get

    # to create box on image 
    new=Image.fromarray(mask)  # converting image from opencv to pillow
    box=new.getbbox()
    
    if box is not None:  # box will have none if no yellow is detected otherwise a range
        x1,y1,x2,y2=box 
        frame=cv.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5) # draw rectangle in green with thickess 5

    cv.imshow('Frame',frame)
    if(cv.waitKey(1) & 0xFF==ord('q')):
       break

cap.release()
cv.destroyAllWindows()