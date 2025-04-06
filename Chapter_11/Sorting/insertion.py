def insertion_sort(arr):
    for i in range (len(arr)):
        j = i 
        while j > 0 and arr[j] < arr[j-1]:
            [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]]
            j -= 1
    

a = [1,3,5,7,2,4,6]
insertion_sort(a)
print(a)