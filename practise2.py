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

def intersection(array_one, array_two):
    array_one_index = 0
    array_two_index = 0
    size_of_array_one = len(array_one)
    size_of_array_two = len(array_two)
    while array_one_index < size_of_array_one and array_two_index < size_of_array_two:
        if array_one[array_one_index] < array_two[array_two_index]:
            array_one_index += 1
        elif array_one[array_one_index] > array_two[array_two_index]:
            array_two_index += 1
        else:
            yield array_one[array_one_index]
            array_one_index += 1
            array_two_index += 1

def union(array_one, array_two):
    array_one_index = 0
    array_two_index = 0
    size_of_array_one = len(array_one)
    size_of_array_two = len(array_two)
    while array_one_index < size_of_array_one and array_two_index < size_of_array_two:
        if array_one_index > 0 and array_one[array_one_index - 1] == array_one[array_one_index]:
            array_one_index += 1
            continue
        if array_two_index > 0 and array_two[array_two_index - 1] == array_two[array_two_index]:
            array_two_index += 1
            continue
        if array_one[array_one_index] < array_two[array_two_index]:
            yield array_one[array_one_index]
            array_one_index += 1
        elif array_one[array_one_index] > array_two[array_two_index]:
            yield array_two[array_two_index]
            array_two_index += 1
        else:
            yield array_one[array_one_index]
            array_one_index += 1
            array_two_index += 1

    while array_two_index < size_of_array_two:
        if array_two_index > 0 and array_two[array_two_index - 1] == array_two[array_two_index]:
            array_two_index += 1
            continue
        yield array_two[array_two_index]
        array_two_index += 1

    while array_one_index < size_of_array_one:
        if array_one_index > 0 and array_one[array_one_index - 1] == array_one[array_one_index]:
            array_one_index += 1
            continue
        yield array_one[array_one_index]
        array_one_index += 1                        