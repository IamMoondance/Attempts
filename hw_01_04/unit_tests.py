#!/usr/bin/env python3

import sys, os
from binary_to_hex import system, adding, convert

# Первая функция

test_in1 = ['1001', '92071', 'E1t1', '101,1011', '111-101', '']
test_out1 = [True, False, False, False, False, True]

hard_test_in1 = [-2]

max1 = len(test_in1) + len(hard_test_in1)
complete1 = 0

# Проверка работы функции при тепличных тестах

print('Normal tests:\n')

for i in range(len(test_in1)):
    if system(test_in1[i]) == test_out1[i]:
        complete1 += 1
        print('Test 1.1.{:} passed'.format(i+1))
    else:
        print('Test 1.1.{:} FAILED'.format(i+1))

# Проверка того, строка ли приходит в функцию на вход

print('\nHard tests:\n')

for i in range(len(hard_test_in1)):
    try:
        system(hard_test_in1[i]);
    except AssertionError:
        complete1 += 1
        print('Test 1.2.{:} passed'.format(i+1))
    else:
        print('Test 1.2.{:} FAILED'.format(i+1))

print('\n{:} of {:} tests 1 unit complete ({:3.2f}%)'.format(complete1, max1,
                                                    complete1*100/max1))

# Вторая функция

test_in2 = ['100011', '11101111', '101010', 'a2', '', '-01']
test_out2 = ['23','EF','2A', 'Incorrect input data', '', 'Incorrect input data']

hard_test_in2 = [-2]

testfile = open("TESTFILE.txt", "w+")

max2 = len(test_in2) + len(hard_test_in2) + 2
complete2 = 0

# Проверка работы функции при тепличных тестах

print('\nNormal tests:\n')

for i in range(len(test_in2)):
    convert(testfile, test_in2[i])
    testfile.seek(0)
    if testfile.readlines()[-1] == test_out2[i]+'\n':
        complete2 += 1
        print('Test 2.1.{:} passed'.format(i+1))
    else:
        print('Test 2.1.{:} FAILED'.format(i+1))

# Проверка того, строка ли приходит в функцию на вход

print('\nHard tests:\n')

for i in range(len(hard_test_in2)):
    try:
        convert(testfile, hard_test_in2[i]);
    except AssertionError:
        complete2 += 1
        print('Test 2.2.{:} passed'.format(i+1))
    else:
        print('Test 2.2.{:} FAILED'.format(i+1))

# Проверка файловой переменной
try:
    convert('cdc', '101');
except AssertionError:
    complete2 += 1
    print('Test 2.2.{:} passed'.format(i+2))
else:
    print('Test 2.2.{:} FAILED'.format(i+2))

testfile.close()
testfile = open("TESTFILE.txt", "r")

# Проверка файла на возможность записи
try:
    convert(testfile, '101');
except AssertionError:
    complete2 += 1
    print('Test 2.2.{:} passed'.format(i+3))
else:
    print('Test 2.2.{:} FAILED'.format(i+3))

testfile.close()
os.remove("TESTFILE.txt")

print('\n{:} of {:} tests 2 unit complete ({:3.2f}%)'.format(complete2, max2,
                                                    complete2*100/max2))

# Cуммарный результат тестирования

print('\n{:} of {:} all tests complete ({:3.2f}%)'
      .format(complete2 + complete1, max2 + max1,
              (complete2 + complete1)*100/(max2 + max1)))
