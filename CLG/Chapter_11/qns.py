people = [
    ("Elon Musk", 433.9),
    ("Jeff Bezos", 239.4),
    ("Mark Zuckerberg", 211.8),
    ("Larry Ellison", 204.6),
    ("Bernard Arnault & Family", 181.3),
    ("Larry Page", 161.4)
]

def selection_sort(data):
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j][1] > arr[max_idx][1]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

# Function to perform bubble sort
def bubble_sort(data):
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Function to perform insertion sort
def insertion_sort(data):
    arr = data.copy()
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j][1] > arr[j - 1][1]:
            [arr[j], arr[j-1]] = [arr[j-1], arr[j]]
            j -= 1
        
    return arr

# Sort using all three algorithms
sorted_selection = selection_sort(people)
sorted_bubble = bubble_sort(people)
sorted_insertion = insertion_sort(people)

# Convert to dictionary
sorted_dict = {name: networth for name, networth in sorted_selection}

# Print result
print(sorted_dict)