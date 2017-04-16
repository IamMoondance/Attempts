arr = list(map(float, input('Массив для сортировки: ').split()))

b = len(arr)-1
a = 0
up = True
k = 0

while b-a>0:
    end = True
    if up:
        for i in range(a, b):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                k = i
                end = False
        b = k
    else:
        for i in range(b, a, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                k = i
                end = False
        a = k
    up = not up
    if end:
        break

print('\nОтсортированный массив:')
for i in arr:
    print(i, end=' ')
