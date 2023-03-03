import cv2
import os
import enum
import math
import yolo_detection_multi
from yolo_detection_multi import multi_object_detect_circle
from sort_yolo_list import sort_neural_list
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

#подгатавливаем данные
path='1wheel_photo'
write_path='1wheel_etalon'
frame_count=1
deviation_list=[]

class Objects(enum.Enum):
    wheel = 0
    laser = 1


while True:

    try:
        img=cv2.imread(os.path.join(path,f'img{frame_count}.jpg'))
        height, width = img.shape[:2]
    except BaseException :
        break

    # открываем файл
    file = open(os.path.join(path, f'img{frame_count}.txt'), mode='r', encoding='utf8')
    line = file.readline()
    file.close()
    list = line.split()

    # конвертируем строку в числа
    number_list = []
    for number in list:
        number_list.append(float(number))
    # <class> <x> <y> <width> <height>

    # получаем абсолютные координаты предмета
    number_list[1] = int(number_list[1] * width)
    number_list[2] = int(number_list[2] * height)
    number_list[3] = int(number_list[3] * width)
    number_list[4] = int(number_list[4] * height)

    etalon_coordinates=[number_list[1],number_list[2]]
    print(etalon_coordinates)
    width_object=number_list[3]
    height_object=number_list[4]


    yolo_list=multi_object_detect_circle(img)




    deviation_from_etalon=sort_neural_list(etalon_coordinates, yolo_list,Objects)
    print(deviation_from_etalon)
    size_diag_object=math.sqrt(width_object**2+height_object**2)
    print(size_diag_object)
    print(f'deviation is {round(deviation_from_etalon/size_diag_object*100,2)}')
    deviation_list.append(round(deviation_from_etalon/size_diag_object*100,2))

    print(yolo_list)


    cv2.circle(img, etalon_coordinates, 10, (0, 255, 0), -1)

    frame_count += 1
    cv2.imshow('result', img)
    cv2.waitKey(100)

print(deviation_list)
fig=plt.figure(figsize=(7,4))
ax1=plt.subplot()
ax1.set_ylim(0,10)
ax1.set_xlim(xmin=0,xmax=len(deviation_list))
ax1.set_xlabel('frame number')
ax1.set_ylabel('deviation in %')
ax1.yaxis.set_major_locator(MultipleLocator(base=1))
ax1.legend(title=f'max deviation is {max(deviation_list)} \n'
                 f'average deviation is {round(sum(deviation_list)/len(deviation_list),2)} \n'
                 f'min deviation is {min(deviation_list)}')
ax1.plot(deviation_list)
fig.suptitle('center deviation in frames for 1 wheel')
plt.grid()
plt.show()