import cv2 
import numpy as np

#Creating a canvas 500 * 500
canvas = np.zeros((500,500,3))

#Drawing a line -> cv2.line(img,pt1,pt2,color,thickness, linetype)
# line 4 and line 8 - bresenham algo
#line AA - Gausian filtering
cv2.line(canvas,(0,0),(100,100),(0,255,0),2,cv2.LINE_4)
cv2.line(canvas,(0,20),(120,120),(0,255,0),2,cv2.LINE_AA)

#Drawing a rectange (start,end, color,thickness)
cv2.rectangle(canvas, (200,200),(250,270),(0,0,255),-1)


#Drawing a Circle 
cv2.circle(canvas,(250,250),10,(250,0,0),3)

#Drawing a Arrowed line (center, radius,bgr, thichkness)
cv2.arrowedLine(canvas,(400,400),(400,500),(255,300,100),tipLength=0.3)


#Showing the canvas
cv2.imshow("winname",canvas)
cv2.waitKey(200000)