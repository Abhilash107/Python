def modified_linear_search(arr, key):
    for i in range(len(arr)-1, -1, -1):# get the last index
        if key == arr[i]:
            return i
    return -1

a = [1,2,3,4,5,3]
res = modified_linear_search(a, 3)
print(res)