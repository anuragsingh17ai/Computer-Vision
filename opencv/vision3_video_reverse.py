import cv2 

cap = cv2.VideoCapture('jj.avi')
opened = cap.isOpened()

forcc = cv2.VideoWriter.fourcc(*'MJPG') ## defining codec format

#Total number of frames in video
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)


fps = cap.get(cv2.CAP_PROP_FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# object to write video
out = cv2.VideoWriter('reversed.avi',forcc,fps,(int(width*0.5),int(height*0.5)))

#finding last frame count as 0 index l
frame_index = frames-1

if opened:
    while frame_index!=0:
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        ret,frame = cap.read()

        # resize the frame 
        frame = cv2.resize(frame,(int(width*0.5),int(height*0.5)))

        #showing video in reverse
        cv2.imshow('video',frame)
        
        #writing the reverse video
        out.write(frame)


        #Decrementing Frame index at each step
        frame_index = frame_index - 1
        if (frame_index%100==0):
            print(frame_index)
        
        if cv2.waitKey(2) == ord('q'):
            break

out.release()
cap.release()
cv2.destroyAllWindows()
