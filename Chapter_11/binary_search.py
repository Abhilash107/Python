def binary_search(arr, key):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l)//2
        
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1

def binary_search_recursive(arr, key, l, r):
    if l > r:
        return -1  # Base case: key not found

    mid = l + (r - l) // 2  # Calculate the midpoint

    if key == arr[mid]:  # Key found
        return mid
    elif key < arr[mid]:  # Search in the left half
        return binary_search_recursive(arr, key, l, mid - 1)
    else:  # Search in the right half
        return binary_search_recursive(arr, key, mid + 1, r)


a = [1,2,3,4,5,6,7,8,9]
# res = binary_search(a, 3)
# print(res)

res = binary_search_recursive(a, 3, 0, len(a)-1)
print(res)