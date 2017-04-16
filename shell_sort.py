arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

k = (len(arr)-1)//2
while k > 0:
    for i in range(k, len(arr)):
        t = arr[i]
        for j in range(i, k-2, -k):
            if t < arr[j-k]:
                arr[j] = arr[j-k]
            else:
                break
        arr[j] = t
    k = k//2
    
print(arr)
