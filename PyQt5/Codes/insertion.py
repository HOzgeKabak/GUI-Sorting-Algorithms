def insertion_sort(Array):
    for j in range(1, len(Array)):
        keyvalue = Array[j]
        i = j - 1
        while i > -1 and Array[i] > keyvalue:
            Array[i + 1] = Array[i]
            i = i - 1
        Array[i + 1] = keyvalue
    return Array