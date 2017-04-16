arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(arr)

for i in range(len(arr)-1):
    min_i = i
    for j in range(i, len(arr)):
        if arr[min_i]>arr[j]:
            min_i = j
    if i != min_i:
        arr[i], arr[min_i] = arr[min_i], arr[i]
    
print(arr)
