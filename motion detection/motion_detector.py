#NOTE: when the code is started make sure the first frame is the background only without any motion body present
import cv2

#change the value of area_val to adjust the motion detection of the object
area_val=30000
count=1
cap=cv2.VideoCapture(0)
_,firstFrame=cap.read()
firstFrame = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    # compute the absolute difference between the current frame and first frame
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    # dilate the thresholded image to fill in holes, then find contours on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)
    _,cnts,_ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        area=cv2.contourArea(c)
        if area>area_val:
            cv2.imwrite('intrution{}.jpg'.format(count),frame)
            cv2.drawContours(frame,c,-1,(255,0,0),3)
            print("intrution detected")
            count+=1
            if count>10:
                count=1
    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
