import cv2
import numpy as np
import time
import enum
import os

#declare object list
class Objects(enum.Enum):
    wheel = 0
    laser = 1

#config yolo
net1 = cv2.dnn.readNet("yolo_sources/multi.weights", "yolo_sources/tiny_multi.cfg")
classes = ["wheel","laser"]
layer_names = net1.getLayerNames()
output_layers = [layer_names[i - 1] for i in net1.getUnconnectedOutLayers()]




def multi_object_detect_rectangle(img):
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net1.setInput(blob)
    outs = net1.forward(output_layers)

    # create lists with object
    class_ids = []
    confidences = []
    boxes = []



    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:
                # Object detected
                # print(class_id)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    #sort out data
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # print(boxes)
    # print(indexes)
    # print(class_ids)

    return_list=[[],[]]
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            x_c=x+w//2
            y_c=y+h//2
            # cv2.circle(img, (x_c, y_c), 10, (0, 0, 255), -1)
            label = str(classes[class_ids[i]])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 2)
            # cv2.putText(img, label, (x, y + 30), font, 3, (0,255,0), 2)
            if class_ids[i]==Objects.wheel.value:
                return_list[Objects.wheel.value].append(boxes[i])
            if class_ids[i]==Objects.laser.value:
                return_list[Objects.laser.value].append(boxes[i])

    return return_list

def multi_object_detect_circle(img):
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net1.setInput(blob)
    outs = net1.forward(output_layers)

    # create lists with object
    class_ids = []
    confidences = []
    boxes = []



    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:
                # Object detected
                # print(class_id)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    #sort out data
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # print(boxes)
    # print(indexes)
    # print(class_ids)

    return_list=[[],[]]
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            x_c=x+w//2
            y_c=y+h//2
            cv2.circle(img, (x_c, y_c), 10, (0, 0, 255), -1)
            label = str(classes[class_ids[i]])
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 2)
            # cv2.putText(img, label, (x, y + 30), font, 3, (0,255,0), 2)
            if class_ids[i]==Objects.wheel.value:
                return_list[Objects.wheel.value].append([x_c,y_c])
            if class_ids[i]==Objects.laser.value:
                return_list[Objects.laser.value].append([x_c,y_c])

    return return_list




if __name__=='__main__':
    path='4wheel_photo'
    frame_count=1
    while True:
        try:
            img=cv2.imread(os.path.join(path,f'img{frame_count}.jpg'))
            img = cv2.resize(img, (640, 480))
            img = cv2.flip(img, 1)
        except BaseException:
            break

        start=time.time()
        return_list=multi_object_detect_circle(img)
        end=time.time()
        cv2.putText(img, "{} fps".format(round(1/(end-start),2)), (20,30), cv2.FONT_HERSHEY_PLAIN, 3, (0,0, 255), 2)
        print(return_list)

        frame_count+=1
        cv2.imshow("Image", img)
        cv2.waitKey(1)