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
from math import sin, cos, log
import matplotlib.pyplot as plt
from prettytable import PrettyTable

'''
def f(x):
    return (sin(x) + 3*x*x - 7*x - 2)

def fs(x):
    return (cos(x) + 3*x - 7)

def fss(x):
    return (-sin(x) + 3)

def fsss(x):
    return (-cos(x))
'''

# Исходная функция и её производные:
def f(x):
    return sin(x)

def fs(x):
    return cos(x)

def fss(x):
    return (-sin(x))

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

x0 = a
x1 = x0 + h

print('\nФункция - sin(x)')
print('\nСпецификация ошибок:')
print('0 - Нет ошибок')
print('1 - Количество итераций превзошло максимум')
print('2 - Невозможно построить касательную')
print('3 - Равенство производной нулю')
print()

table = PrettyTable(["№", "x0", "x1", "x", "f(x)", "iters", "error"])

# Включение подсчёта времени:
time_start = perfc()

i = 1
while x1 <= b:
    if f(x0)*f(x1) <= 0:
        pr = fs(x0)
        xl, xr = x0, x1
        counter = 1
        while (xr - xl) > eps:
            if pr == 0:
                break
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
                if pr == 0:
#                    table.add_row([i,'{:0.5f}'.format(xl),'{:0.5f}'.format(xr),
#                                  '-','-','-','3'])
                    table.add_row([i,'{:0.5f}'.format(x0),'{:0.5f}'.format(x1),
                                  '-','-','-','3'])
                    break
                xr = xr - f(xr)/pr
                # Вывод ошибки построения касательной:
                if xr > x1:
#                    table.add_row([i,'{:0.5f}'.format(xl),'{:0.5f}'.format(xr),
#                                   '-','-','-','2'])
                    table.add_row([i,'{:0.5f}'.format(x0),'{:0.5f}'.format(x1),
                                   '-','-','-','2'])
                    i += 1
                    break
                # Вывод ошибки превышения числа итераций:
                if counter == max_iter:
#                    table.add_row([i,'{:0.5f}'.format(xl),'{:0.5f}'.format(xr),
#                                   '-','-',counter,'1'])
                    table.add_row([i,'{:0.5f}'.format(x0),'{:0.5f}'.format(x1),
                                   '-','-',counter,'1'])
                    i += 1
                    break
                else:
                    counter += 1
        # Вывод случаев, которые не имеют ошибок:
        if (xr - xl) < eps:
            x_arr.append((xr+xl)/2)
            table.add_row([i,'{:0.5e}'.format(xl),'{:0.5e}'.format(xr),
                  '{:0.5e}'.format(x_arr[-1]),'{:0.5e}'.format(f(x_arr[-1])),
                  counter,'0'])
            i += 1

    if x0 + h < b:
        x0 += h
        x1 += h
        if x1 > b:
            x1 = b
    else:
        break

x0 = a
x1 = x0 + h
while x1 <= b:
    if fs(x0)*fs(x1) <= 0:
        pr = fss(x0)
        xl, xr = x0, x1
        counter = 1
        while (xr - xl) > eps:
            if pr == 0:
                break
            xl = xl - fs(xl)/pr
            if xl < x0:
                break
            if counter == max_iter:
                break
            else:
                counter += 1
        if (xr - xl) > eps:
            pr = fss(x1)
            xl, xr = x0, x1
            counter = 1
            while (xr - xl) > eps:
                if pr == 0:
                    break
                xr = xr - fs(xr)/pr
                if xr > x1:
                    break
                if counter == max_iter:
                    break
                else:
                    counter += 1
        if 0 <= (xr - xl) < eps:
            x_arr_fs.append((xr+xl)/2)
    
    if x0 + h < b:
        x0 += h
        x1 += h
        if x1 > b:
            x1 = b
    else:
        break

x0 = a
x1 = x0 + h
while x1 <= b:
    if fss(x0)*fss(x1) <= 0:
        pr = fsss(x0)
        xl, xr = x0, x1
        counter = 1
        while (xr - xl) > eps:
            if pr == 0:
                break
            xl = xl - fss(xl)/pr
            if xl < x0:
                break
            if counter == max_iter:
                break
            else:
                counter += 1
        if (xr - xl) > eps:
            pr = fsss(x1)
            xl, xr = x0, x1
            counter = 1
            while (xr - xl) > eps:
                if pr == 0:
                    break
                xr = xr - fss(xr)/pr
                if xr > x1:
                    break
                if counter == max_iter:
                    break
                else:
                    counter += 1
        if 0 <= (xr - xl) < eps:
            x_arr_fss.append((xr+xl)/2)
    
    if x0 + h < b:
        x0 += h
        x1 += h
        if x1 > b:
            x1 = b
    else:
        break

print(table)
print()
print('Время, требуемое на выполнение:')
print('{:0.5f}'.format(perfc() - time_start),'секунд')

for i in range(len(x_arr)):
    y_arr.append(f(x_arr[i]))
    #print(x_arr[i],y_arr[i])

# График и корни:
plt.axhline(0, color='black')
plt.axvline(0, color='black')
x_iter = [a+i*(b-a)/1000 for i in range(1000)]
plt.plot(x_iter,[f(i) for i in x_iter])
plt.plot(x_arr, y_arr, ls='', marker='o', color='b', label='roots')
# Точки экстремума:
if len(x_arr_fs) > 0:
    y_arr_fs = [f(i) for i in x_arr_fs]
    plt.plot(x_arr_fs, y_arr_fs, marker='x', ls='', color='c', label='exterems')
# Точки перегиба:
if len(x_arr_fss) > 0:
    y_arr_fss = [f(i) for i in x_arr_fss]
    plt.plot(x_arr_fss, y_arr_fss, marker='*', ls='', color='y',label='excesses')
# Точки максимума и минимума:
if len(x_arr_fs) > 1:
    plt.plot([x_arr_fs[y_arr_fs.index(max(y_arr_fs))]], \
             [max(y_arr_fs)], marker='v', ls='', color='g',label='maximum')
    plt.plot([x_arr_fs[y_arr_fs.index(min(y_arr_fs))]],\
             [min(y_arr_fs)], marker='^', ls='', color='r',label='minimum')
elif len(x_arr_fs) == 1:
    if y_arr_fs[0] > 0:
        plt.plot([x_arr_fs[0]], [y_arr_fs[0]],
                 marker='v', ls='', color='g',label='maximum')
    else:
        plt.plot([x_arr_fs[0]], [y_arr_fs[0]],
                 marker='^', ls='', color='r',label='minimum')

plt.legend(loc=0)
plt.xlim(a, b)
plt.show()
