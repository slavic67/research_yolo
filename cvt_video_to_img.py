import cv2
import os

cap=cv2.VideoCapture('sources/4wheels.MOV') 
fl=True
frame=1
frame_count=1
path='4wheel_photo'
while fl:
    fl,img=cap.read()
    if fl:
        img=cv2.resize(img,(480,640))
        img= cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite('sources/img{}.jpg'.format(a),img)
        frame+=1
        if frame%5==0:
            cv2.imwrite(os.path.join(path,f'img{frame_count}.jpg'),img)
            frame_count+=1

        cv2.imshow('result',img)
        cv2.waitKey(1)
print(frame)
print(frame_count)