import time
from colors import *

def merge(data, start, mid, end, drawData, timeTick):
    arr_temp = []
    ending = mid + 1
    starting = start
    

    for i in range(start, end+1):
        if starting > mid:
            arr_temp.append(data[ending])
            ending+=1
        elif ending > end:
            arr_temp.append(data[starting])
            starting+=1
        elif data[starting] < data[ending]:
            arr_temp.append(data[starting])
            starting+=1
        else:
            arr_temp.append(data[ending])
            ending+=1

    for starting in range(len(arr_temp)):
        data[start] = arr_temp[starting]
        start += 1

def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data, mid+1, end, drawData, timeTick)

        merge(data, start, mid, end, drawData, timeTick)

        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                        else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
