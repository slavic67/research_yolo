import cv2
import os

#подгатавливаем данные
path='1wheel_photo'
write_path='1wheel_etalon'
frame_count=1

while True:

    try:
        img=cv2.imread(os.path.join(path,f'img{frame_count}.jpg'))
        height, width = img.shape[:2]
    except BaseException :
        break


    #print(height,width)

    #открываем файл
    file=open(os.path.join(path,f'img{frame_count}.txt'),mode='r',encoding='utf8')
    line=file.readline()
    list=line.split()

    #конвертируем строку в числа
    number_list=[]
    for number in list:
        number_list.append(float(number))
    # <class> <x> <y> <width> <height>
    #print(number_list)

    #получаем абсолютные координаты предмета
    number_list[1]=int(number_list[1] * width)
    number_list[2]=int(number_list[2] * height)
    number_list[3]=int(number_list[3] * width)
    number_list[4]=int(number_list[4] * height)
    #------------------------------------------
    rec_coordinates=[0,0,0,0]
    rec_coordinates[0]=number_list[1]-number_list[3]//2
    rec_coordinates[1]=number_list[2]-number_list[4]//2
    rec_coordinates[2]=number_list[1]+number_list[3]//2
    rec_coordinates[3]=number_list[2]+number_list[4]//2



    # cv2.circle(img, (number_list[3], number_list[4]), 5, (0, 0, 255), thickness=-1)
    cv2.rectangle(img,(rec_coordinates[0],rec_coordinates[1]), \
                  (rec_coordinates[2],rec_coordinates[3]),(0,255,0),thickness=2)

    file.close()
    cv2.imwrite(os.path.join(write_path,f'img{frame_count}.jpg'), img)
    frame_count+=1

    cv2.imshow('result',img)
    cv2.waitKey(100)