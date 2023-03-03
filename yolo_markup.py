import cv2
import time
import yolo_detection_multi
from yolo_detection_multi import multi_object_detect_rectangle
import os


path='etalons/4wheel_etalon'
write_path='4_etalon+yolo'
frame_count=1
while True:
    try:
        img=cv2.imread(os.path.join(path,f'img{frame_count}.jpg'))
        img = cv2.resize(img, (640, 480))
        img = cv2.flip(img, 1)
    except BaseException:
        break

    start=time.time()
    return_list=multi_object_detect_rectangle(img)
    end=time.time()
    # cv2.putText(img, "{} fps".format(round(1/(end-start),2)), (20,30), cv2.FONT_HERSHEY_PLAIN, 3, (0,0, 255), 2)
    cv2.putText(img, "red - neural network", \
                (20, 30), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
    cv2.putText(img, "green - etalon", \
                (20, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    print(return_list)

    cv2.imwrite(os.path.join(write_path, f'img{frame_count}.jpg'), img)
    frame_count+=1
    cv2.imshow("Image", img)
    cv2.waitKey(1)