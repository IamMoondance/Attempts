"""
@author: Шибанова Дарья, ИУ7-22
 
Задан текстовый файл, каждая строка которого может рассматриваться
как запись целого числа в двоичной системе счисления.
На его основе создайте текстовый файл, в каждой строке которого необходимо
записать число в шестнадцатеричной системе счисления.
"""

import os.path, sys, io

conv_table =  {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
               '0100': '4', '0101': '5', '0110': '6', '0111': '7',
               '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
               '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

def system(line):
    """
    Проверяет строку на наличие символов, отличных от 1 и 0

    :param line: строка для проверки
    :type line: str
    :rtype: True/False

    """
    assert(type(line) == str)
        
    for i in range(len(line)):
        if not ((line[i] == '1') or (line[i] == '0')):
            return False
    return True

def adding(line):
    """
    Добавляет нули перед числом для перевода по тетрадам

    :param line: строка в двоичной системе, подготавливаемая для перевода
    :type line: str
    :rtype: строка
    
    """
    if len(line)%4 != 0:
        line = '0'*(4-len(line)%4) + line
    return line

def convert(file, line):
    """
    Переводит число по тетрадам из двоичной системы счисления
    в шестнадцатеричную

    :param file: файловая переменная
    :type file: io.TextIOWrapper
    :param line: строка в двоичной системе для перевода
    :type line: str
    :rtype: строка, записываемая в файл
    
    """
    assert(type(file) == io.TextIOWrapper)
    assert(file.mode[0] == 'w' or file.mode[0] == 'a')
    
    if line == '':
        file.write('\n')
        return
    if not system(line):
        file.write('Incorrect input data\n')
        return
    line = adding(line)
    for i in range(len(line)//4):
        original = line[i*4:(i+1)*4]
        converted = conv_table.get(original)
        file.write(converted)
    file.write('\n')

def reading(file1, file2):
    """
    Считывает строки исходного файла

    :param file1: файловая переменная исходного файла
    :type file1: io.TextIOWrapper
    :param file2: файловая переменная файла с результатами выполнения программы
    :type file2: io.TextIOWrapper
    
    """
    for line in file1:
        if line[-1] == '\n':
            line = line[:-1]
        convert(file2, line)

if __name__ == "__main__":
    name1 = input('Enter the input filename: ')
    while not os.path.isfile(name1):
        name1 = input('Enter the filename again (the file is not exist): ')
        
    file1 = open(name1, 'r+')

    name2 = input('Enter the output filename: ')
    while name2 == name1:
        name2 = input('A name of the output is equivalent to the input. \
    Enter another: ')
        
    file2 = open(name2, 'w')

    if file1.readline() == '':
        print('The source file is empty')
        exit()
    file1.seek(0)

    reading(file1, file2)

    print('All tasks are done')

    file1.close()
    file2.close()
