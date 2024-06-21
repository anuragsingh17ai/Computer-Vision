import cv2

### Channel order is BGr in color mode
# image = cv2.imread('image.jpg',cv2.IMREAD_COLOR)   # origninal color
# image = cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)  # grey scale colr
image = cv2.imread('image.jpg',cv2.IMREAD_UNCHANGED)
#####displaying image
cv2.imshow('Display image',image)
cv2.waitKey(500)