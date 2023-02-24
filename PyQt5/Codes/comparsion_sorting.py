#Halime Özge Kabak 180403001
#Comparison For HW1
from insertion import insertion_sort
import numpy as np
import time
import matplotlib.pyplot as plt
from Merge import mergeSort
from Bubble_1 import bubble_sort
elements = list()
times = list()
for i in range(1, 10):
    # generate some integers
    a = np.random.randint(0,(100 * i), 100 * i)
    # print(i)
    start = time.clock()
    insertion_sort(a)
    end = time.clock()


    elements.append(len(a))
    times.append(end - start)

plt.plot(elements,times,color="g")

melements = list()
mtimes = list()
for i in range(1, 10):
    # generate some integers
    a = np.random.randint(0,(100 * i), 100 * i)
    # print(i)
    start = time.clock()
    mergeSort(a,1,len(a)-1)
    end = time.clock()


    melements.append(len(a))
    mtimes.append(end - start)

plt.plot(melements,mtimes,color="m")

belements = list()
btimes = list()
for i in range(1, 10):
    # generate some integers
    a = np.random.randint(0,(100 * i), 100 * i)
    # print(i)
    start = time.clock()
    bubble_sort(a)
    end = time.clock()


    belements.append(len(a))
    btimes.append(end - start)

plt.plot(belements,btimes,color="b")
plt.xlabel('Length')
plt.ylabel('Time')
plt.title("Comparison")
plt.show()