def merge_sort(arr, low , high):
    if low >= high:
        return
    
    mid = low + (high - low)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    res = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j += 1
    
    while i <= mid:
            res.append(arr[i])
            i += 1
    while j <= high:
            res.append(arr[j])
            j += 1
    
    for x in range(len(res)):
        arr[low + x] = res[x]


a = [2, 1, 4, 3, 5, 6]
merge_sort(a, 0, len(a) - 1)
print(a)

    