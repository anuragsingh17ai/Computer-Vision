import cv2 
import numpy as np


#Making a empty black canva
#Here canvas is of three layer
canvas = np.zeros((500,500,3))

#Required points we need to join
pts = np.array([[250,5],[220,80,],[100,50]])

#Reshape the points to shape (number_vertex, 1, 2)
pts = pts.reshape((-1,1,2))


#Draw this polygon
#Here Boolean True and False determine if the figure is closed
cv2.polylines(canvas,[pts], True, (0,255,0), 3)

#showing the canvas
cv2.imshow('win',canvas)
cv2.waitKey(20000)

