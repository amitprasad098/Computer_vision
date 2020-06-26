import numpy as np
import cv2

cap = cv2.VideoCapture(0)
img_counter = 0
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))


while(cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('t'):
	print("EXIT")            
	break
    if ret==True:
        #frame = cv2.flip(frame,0)
	frame2 = cv2.flip(frame, +1);
        # write the flipped frame
        out.write(frame2)
	cv2.imshow('Frame', frame2)
	
        if cv2.waitKey(1) & 0xFF == ord('q'):
        
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

        
	
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
