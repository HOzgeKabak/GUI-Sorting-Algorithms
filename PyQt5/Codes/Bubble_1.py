
def bubble_sort(arr):

    n = len(arr)
    for i in range(0, n-1):
        for j in range(1, n - i):
         if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]