import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

cv2.imwrite('img1.png',frame)
rframe = cv2.imread('img1.png')
gray = cv2.cvtColor(rframe, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
gray = cv2.line(gray,(344,56),(511,511),(100,140,100),3)
gray = cv2.rectangle(gray,(384,0),(510,128),(255,100,255),-5)


while(True):
    cv2.imshow('frame1',gray)
    cv2.imshow('frame2', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
# When everything done, release the capture

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()


vid = cv2.VideoCapture('output.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output2.avi',fourcc, 20.0, (640,480))
while(vid.isOpened()):
    ret, frame = vid.read()
    if (cv2.waitKey(30) & 0xFF == ord('q')) or not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    gray = cv2.line(gray, (344, 56), (511, 511), (100, 140, 100), 3)
    gray = cv2.rectangle(gray, (384, 0), (510, 128), (255, 100, 255), -5)
    out.write(gray)
    cv2.imshow('CAMERA',gray)


vid.release()
cv2.destroyAllWindows()
