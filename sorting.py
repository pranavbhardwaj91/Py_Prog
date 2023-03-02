arr = [3, 56, 67, 31, 2324, 6454, 3453, 2, 235, 546, 37, 78, 34, 345, 345, 2346, 867]

def bubbleSort(arr):
    n = len(arr)
    print("Length of array is: " + str(len(arr)))
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
