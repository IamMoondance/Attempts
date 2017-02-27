#Шибанова Дарья ИУ7-22
#Работа с файлом (содержание которого государства и их государственные языки),
#создание меню, состояющего из пунктов:
# 1) создание файла;
# 2) добавление записи в файл;
# 3) поиск и результат;
# 4) вывод всего содержимого файла;
# 5) выход.

choice = None

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
    try:
        choice = int(input('Выберете один из предложенных вариантов: '))
    except:
        choice = 0
    if choice == 0:
        print('Выполнен выход')
    if choice == 1:
        print('Введите название для файла, заканчивая точкой и форматом: ')
        Name = str(input())
        V1 = open(Name,'w')
        V1.close()
    if choice == 2:
        print()
        V2 = open('states and languages.txt','a+')
        n = int(input('Введите число строк, которые хотите добавить в файл: '))
        print('Введите строки, которые хотите добавить (по одной в строке): ')
        for i in range(n):
            rec = input()
            V2.write(rec +'\n')
        V2.seek(0)
        base2 = V2.readline()
        while base2 != '':
            print(base2,end='')
            base2 = V2.readline()
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
            Rez = open('Rez.txt','w')
            Rez.write("Ищем '"+phrase+"' "+['',"везде","среди языков","среди стран"][where]+"\n")
            base3 = V3.readline()
            while base3 != '':
                if where == 1:
                    rec = base3
                else:
                    rec = base3.split(' - ')[3-where]
                if phrase in rec:
                    print(base3,end='')
                    Rez.write(base3)
                    count += 1
                base3 = V3.readline()
            print('Найдено записей:',count)
            Rez.write('\nНайдено записей: '+str(count))
            Rez.close()

            print()
    #Выводим всё содержимое файла:
    if choice == 4:
        print()
        print('Страна и государственный язык:')
        print()
        V4 = open('states and languages.txt','r')
        base = V4.readline()
        while base != '':
            print(base,end='')
            base = V4.readline()
        V4.close()
        print()
