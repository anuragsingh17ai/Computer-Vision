import cv2 
import numpy as np


#Creating a canvas of 800 * 500 (three Channels)
canvas = np.zeros((800,500))


#list of all fonts
fonts = [cv2.FONT_HERSHEY_COMPLEX,
         cv2.FONT_HERSHEY_PLAIN,
         cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
         cv2.FONT_HERSHEY_TRIPLEX,
         cv2.FONT_HERSHEY_DUPLEX,
         cv2.FONT_HERSHEY_COMPLEX_SMALL]

position = (10,30)
for i in range(0,6):
    cv2.putText(canvas, "THis is OPENCV!",position,fonts[i],1.1,(255,255,255),2,cv2.LINE_AA)
    position= (position[0] , position[1]+40)
    cv2.putText(canvas, "This is OpenCv!".lower(), position,fonts[i],1.1,(255,255,255),2,cv2.LINE_8)
    position = (position[0],position[1]+40)

#Displaying the canvas
cv2.imshow('winname',canvas)
cv2.waitKey(20000)