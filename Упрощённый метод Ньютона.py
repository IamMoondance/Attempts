#Шибанова Дарья ИУ7-22
# Метод: упрощённый метод Ньютона.
# 1. Уточнение корней уравнения. Задание большого отрезка,
#     шага, точности, максимального числа итераций.
#     Вывести: полученный корень, значение функции в точке корня
#     по спецификации типа e с минимальным числом цифр в мантиссе,
#     реальное число операций, код ошибки, исходная функция.
#     Вывод таблицей.
#     Вычислить время выполнения программы.
# 2. Сделать графическое представление функции. Отметить найденные
#     корни, экстремумы, максимумы и минимумы функции, точки перегиба.

from time import perf_counter as perfc
from math import sin, cos
import matplotlib.pyplot as plt

def f(x):
    return (sin(x) + 3*x*x - 7*x + 2)

def fs(x):
    return (cos(x) + 3*x - 7)

def fss(x):
    return (-sin(x) + 3)

def fsss(x):
    return (-cos(x))

a, b = map(float, input('Введите границы интервала (через пробел): ').split())
eps = float(input('Введите точность: '))
max_iter = int(input('Введите максимальное число итераций: '))
h = float(input('Введите шаг: '))

x_arr = list() # y ~= 0 = f(x)
y_arr = list() # y ~= 0
x_arr_fs = list()
x_arr_fss = list()
x_arr_fsss = list()

x0 = a
x1 = x0 + h

time_start = perfc()

print('Спецификация ошибок:')
print('0 - Нет ошибок')
print('1 - Количество итераций превзошло максимум')
print('2 - Невозможно построить касательную')

print('№','x','f(x)','iters','error','function')

while x1 <= b:
    if f(x0)*f(x1) <= 0:
        pr = fs(x0)
        xl, xr = x0, x1
        counter = 1
        while (xr - xl) > eps:
            xl = xl - f(xl)/pr
            if xl < x0:
                break
            if counter == max_iter:
                break
            else:
                counter += 1
        if (xr - xl) > eps:
            pr = fs(x1)
            xl, xr = x0, x1
            counter = 1
            while (xr - xl) > eps:
                xr = xr - f(xr)/pr
                if xr > x1:
                    print('Невозможно построить касательную')
                    break
                if counter == max_iter:
                    print('Количество итераций превзошло максимум')
                    break
                else:
                    counter += 1
        if (xr - xl) < eps:
            x_arr.append((xr+xl)/2)
            print(x_arr[-1])

    
    if x0 + h < b:
        x0 += h
        x1 += h
        if x1 > b:
            x1 = b
    else:
        break

print(perfc() - time_start)

for i in range(len(x_arr)):
    y_arr.append(f(x_arr[i]))
    print(x_arr[i],y_arr[i])

# График и корни:
x_iter = [a+i*(b-a)/1000 for i in range(1000)]
plt.plot(x_iter,[f(i) for i in x_iter])
plt.plot(x_arr, y_arr, ls='', marker='o', color='b')
# Точки экстремума:
y_arr_fs = [f(i) for i in x_arr_fs]
plt.plot(x_arr_fs, y_arr_fs, marker='x', ls='', color='c')
# Точки перегиба:
y_arr_fss = [f(i) for i in x_arr_fss]
plt.plot(x_arr_fss, y_arr_fss, marker='*', ls='', color='y')
# Точки максимума и минимума:
plt.plot([x_points_fs[y_arr_fs.index(max(y_arr_fs))]], \
         [max(y_arr_fs)], marker='v', ls='', color='g')
plt.plot([x_arr_fs[y_arr_fs.index(min(y_arr_fs))]],\
         [min(y_arr_fs)], marker='^', ls='', color='r')
plt.show()
