def swap(array, indexI, indexJ):
    temp = array[indexI]
    array[indexI] = array[indexJ]
    array[indexJ] = temp

def bubbleSort(array):
    n = len(array)
    for indexI in range(n):
        exchanges = 0
        for indexJ in range(n-1, indexI, -1):
            if array[indexJ] < array[indexJ-1]:
                swap(array, indexJ, indexJ-1)
                exchanges += 1
        if exchanges == 0:
            break
def intersection(arrayOne, arrayTwo):
    arrayOneIndex = 0
    arrayTwoIndex =0
    sizeOfArrayOne = len(arrayOne)
    sizeOfArrayTwo = len(arrayTwo)
    array = []
    while arrayOneIndex < sizeOfArrayOne and arrayTwoIndex < sizeOfArrayTwo:
        if arrayOne[arrayOneIndex] < arrayTwo[arrayTwoIndex]:
            arrayOneIndex += 1
        elif arrayOne[arrayOneIndex] > arrayTwo[arrayTwoIndex]:
            arrayTwoIndex += 1
        else:
            array.append(arrayOne[arrayOneIndex])
            arrayOneIndex += 1
            arrayTwoIndex += 1
    return array

def union(arrayOne, arrayTwo):
    arrayOneIndex = 0
    arrayTwoIndex =0
    sizeOfArrayOne = len(arrayOne)
    sizeOfArrayTwo = len(arrayTwo)
    array = []
    while arrayOneIndex < sizeOfArrayOne and arrayTwoIndex < sizeOfArrayTwo:
        if arrayOne[arrayOneIndex] < arrayTwo[arrayTwoIndex]:
            array.append(arrayOne[arrayOneIndex])
            arrayOneIndex += 1
        elif arrayOne[arrayOneIndex] > arrayTwo[arrayTwoIndex]:
            array.append(arrayTwo[arrayTwoIndex])
            arrayTwoIndex += 1
        else:
            array.append(arrayOne[arrayOneIndex])
            arrayOneIndex += 1
            arrayTwoIndex += 1
    if arrayOneIndex == sizeOfArrayOne:
        while arrayTwoIndex < sizeOfArrayTwo:
            array.append(arrayTwo[arrayTwoIndex])
            arrayTwoIndex += 1
    else:
        while arrayOneIndex < sizeOfArrayOne:
            array.append(arrayOne[arrayOneIndex])
            arrayOneIndex += 1
    return array

if __name__ == '__main__':
    sizeOne = int(input())
    try:
        arrayOne = [int(x) for x in input().split()]
    except:
        print('Invalid input')
        sys.exit()
    sizeTwo = int(input())
    try:
        arrayTwo = [int(x) for x in input().split()]
    except:
        print('Invalid syntax')
        sys.exit()
    bubbleSort(arrayOne)
    bubbleSort(arrayTwo)
    intersectionArray = intersection(arrayOne, arrayTwo)
    unionArray = union(arrayOne, arrayTwo)
    print(*unionArray, sep=" ")
    print(*intersectionArray, sep=" ")