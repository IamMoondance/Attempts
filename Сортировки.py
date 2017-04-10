# Шибанова Дарья ИУ7-22
# Сортировка улучшенным методом пузырька
# Сортировка встроенной функцией sorted

from time import perf_counter as perfc
from random import randint

def bubble_optimized(i_arr):
    arr = i_arr[:]
    for i in range(len(arr)-1, 1, -1):
        flag = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = True
        if not flag:
            break
    return arr

def bubble_optimized2(i_arr):
    arr = i_arr[:]
    i = len(arr)-1
    while i >= 1:
        flag = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = True
                k = j
        if not flag:
            break
        else:
            i = k
    return arr

def bubble(i_arr):
    arr = i_arr[:]
    for i in range(len(arr)-1, 1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

def sort(i_arr):
    arr = i_arr[:]
    return sorted(arr)

c = None
while c != 0:

    print('Выберете, каким способом задаётся целочисленный массив:')
    print('''
    1 - введённый по умолчанию пример
    2 - введённый по умолчанию пример (отсортированный по возрастанию)
    3 - введённый по умолчанию пример (отсортированный по убыванию)
    4 - ручной ввод
    5 - создание с помощью рандома
    0 - выйти из программы
    ''')

    c = int(input())
    if c == 1:
        arr = [1, 3, 6, 9, 7, 8, 4, 5, 2]
    elif c == 2:
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    elif c == 3:
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    elif c == 4:
        arr = []
        n = int(input('Введите, какой длины хотите задать массив: '))
        print('Введите числа (по одному в строке): ')
        for i in range(n):
            a = int(input())
            arr.append(a)
    elif c == 5:
        n = int(input('Введите, из скольких элементов составить список: '))
        a, b = map(int, input('Введите начало и конец промежутка \
для выбора (через пробел): ').split())
        arr = [randint(a, b) for i in range(n)]
    elif c == 0:
        print('Выполнен выход из программы')
        break

    print()
    print('Исходный массив:')
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()
    print()

    stime = perfc()
    print('Метод пузырька:')
    for i in range(len(arr)):
        print(bubble(arr)[i], end=' ')
    print()
    print('Время на выполнение:')
    print('{:0.5f}'.format(perfc() - stime),'секунд на',len(arr),'элементов')
    print()

    stime = perfc()
    print('Улучшенный метод пузырька с одним изменением:')
    for i in range(len(arr)):
        print(bubble_optimized(arr)[i], end=' ')
    print()
    print('Время на выполнение:')
    print('{:0.5f}'.format(perfc() - stime),'секунд на',len(arr),'элементов')
    print()

    stime = perfc()
    print('Улучшенный метод пузырька с двумя изменениями:')
    for i in range(len(arr)):
        print(bubble_optimized2(arr)[i], end=' ')
    print()
    print('Время на выполнение:')
    print('{:0.5f}'.format(perfc() - stime),'секунд на',len(arr),'элементов')
    print()

    stime = perfc()
    print('С помощью встроенной функции sorted():')
    for i in range(len(arr)):
        print(sort(arr)[i], end=' ')
    print()
    print('Время на выполнение:')
    print('{:0.5f}'.format(perfc() - stime),'секунд на',len(arr),'элементов')
    print()
