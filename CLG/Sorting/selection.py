def selection_sort(arr):
    for i in range (len(arr)):
        minElement = i
        for j in range (i, len(arr)):
            if arr[j] < arr[minElement]:
                minElement = j# get smallest
        
        [arr[i], arr[minElement]] = [arr[minElement], arr[i]]# SWAP

a = [1,3,5,7,2,4,6]
selection_sort(a)
print(a)