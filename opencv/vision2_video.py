import cv2 

cap = cv2.VideoCapture(0)

opened = cap.isOpened()

# fourcc
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv2.CAP_PROP_FPS)




# video writer
out = cv2.VideoWriter('jj.avi',fourcc,fps,(int(width),int(height)))



print(height,width)
print("Frames are {}".format(fps))

if opened:
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            cv2.imshow('video',frame)
            out.write(frame)
            if cv2.waitKey(2) == 27:
                break

out.release()
cap.release()
cv2.destroyAllWindows()

