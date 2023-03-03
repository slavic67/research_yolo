import math

def sort_neural_list(etalon_coordinates,yolo_list,Objects):

    min_delta=etalon_coordinates
    for i in range(len(yolo_list[Objects.wheel.value])):
        delta=[0,0]
        delta[0]=abs(etalon_coordinates[0]-yolo_list[Objects.wheel.value][i][0])
        delta[1] = abs(etalon_coordinates[1] - yolo_list[Objects.wheel.value][i][1])
        if delta[0]<min_delta[0] and delta[1]<min_delta[1]:
            min_delta=delta

    deviation_from_etalon=math.sqrt(min_delta[0]**2+min_delta[1]**2)

    return round(deviation_from_etalon,2)