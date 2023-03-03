import cv2
import numpy as np
import os

#прописываем пути
path='4_etalon+yolo'
write_path='1wheel_etalon'
frame_count=1
#делаем настройки для выходного видео
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('4_etalon+yolo.avi',fourcc, 20.0, (640,480))

i=0
while True:
    try:
        img=cv2.imread(os.path.join(path,f'img{frame_count}.jpg'))
        _,_,_=img.shape

    except BaseException:
        print('done')
        break


    i+=1
    out.write(img)
    if i>3:
        frame_count+=1
        i=0
out.release()
cv2.destroyAllWindows()
