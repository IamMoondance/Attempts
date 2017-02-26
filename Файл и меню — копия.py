#Шибанова Дарья ИУ7-22
#Работа с файлом (содержание которого государства и их государственные языки),
#создание меню, состояющего из пунктов:
# 1) создание файла;
# 2) добавление записи в файл;
# 3) поиск и результат;
# 4) вывод всего содержимого файла;
# 5) выход.

choice = None
V4 = open('states and languages.txt','r')
base = V4.readline()
while base != '':
    base = V4.readline()
V4.close()
while choice != 0:
    print('Меню:')
    print(
    '''
    0 - Выход
    1 - Создание файла
    2 - Добавление записи в файл
    3 - Поиск информации и результат
    4 - Вывод всего содержимого файла
    '''
    )

    choice = int(input('Выберете один из предложенных вариантов: '))
    if choice == 0:
        print('Выполнен выход')
    if choice == 1:
        print('Введите название для файла, заканчивая точкой и форматом: ')
        Name = str(input())
        V1 = open(Name,'w')
    if choice == 2:
        print()
        V2 = open('states and languages.txt','a+')
        n = int(input('Введите число строк, которые хотите добавить в файл: '))
        print('Введите строки, которые хотите добавить (по одной в строке): ')
        V2.seek(0)
        for i in range(n):
            rec = input()
            V2.write(rec +'\n')
        V2.close()
        V2 = open('states and languages.txt','r')
        V2.seek(0)
        base2 = V2.readline()
        while base2 != '':
            base2 = V2.readline()
        for i in range(len(base2)):
            print(base2[i],end='')
        V2.close()
        print()
    if choice == 3:
        print(
            '''
    0 - Не искать
    1 - Искать везде
    2 - Искать среди языков
    3 - Искать среди стран
            '''
            )
        print('Если записи не окажется, в файл добавится весь список записей.')
        print('Пожалуйста, выберете, введя цифру, где производить поиск: ')
        where = int(input())
        count = 0
        #Проверяем, нужно ли производить поиск:
        if where == 0:
            print('Поиск не был произведён')
        else:
            phrase = input('Введите искомое значение: ')
            V3 = open('states and languages.txt','r')
            V3.seek(0)
            base3 = V3.readline()
            while base3 != '':
                base3 = V3.readline()
            for i in base3:
                if where == 1:
                    rec = i
                else:
                    rec = i.split(' - ')[3-where]
                    Rez = open('Rez.txt','a')
                    Rez.write(i + '\n')
                    Rez.close()
                if phrase in rec:
                    print(i,end='')
                    Rez = open('Rez.txt','a')
                    Rez.write(i + '\n')
                    count += 1
                    Rez.close()
            print('Найдено записей:',count)

            print()
    #Выводим всё содержимое файла:
    if choice == 4:
        print()
        print('Страна и государственный язык:')
        print()
        V4 = open('states and languages.txt','r')
        for i in range(len(base)):
            print(base[i],end='')
        V4.close()
        print()
