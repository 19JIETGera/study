#Создать телефонный справочник с возможностью импорта и экспорта данных в
#формате .txt фамилия, имя отчество, номер телефона данные которые должны находиться в файле
#1. Программа должна выводить данные
#2. Программа должна сохранять данные в текстовом файле
#3. Пользователь может ввести одну из характеристик для поиска определенной записи
#4. Использование функций
#Ваша программа не должна быть линейной
#Дополнить телефонный справочник возможностью изменения и удаления данных.
#Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
from pathlib import Path
file_path = Path('directory.txt')

def Read_File():
    with open(file_path, 'r') as f:
        for line in f:
            print(line, end='')


def Append_File():
    with open(file_path, 'a') as f:
        f.write('\n' + input('Введите данные для записи в телефонную книгу через "," по типу Имя,Фамилия,номер телефона (+7*********) (без пробелов)\n'))

def Deleted_File():
    with open(file_path, 'r') as f:
        lines = f.readlines()
        Read_File()
        input_people = input('\nВыберите чьи данные вы хотите удалить (напишите их в точности как в образце перед вами)\n')
        Deleted_Date(lines, input_people)
        print('Удалено\n')

def Deleted_Date(lines, i):
    with open(file_path, 'w') as fw:
        for line in lines:
            if line.strip('\n') != i:
                fw.write(line)

def Change_File():
    with open(file_path, 'r') as f:
        b = False
        lines = f.readlines()
        Read_File()
        input_people = input('\nВыберите чьи данные вы хотите поменять (напишите их в точности как в образце перед вами)\n')
        b = Change_Date(lines, input_people)
        if not b:
            print('Такого контакта нет')
            return Change_File()

def Change_Date(lines, input_people):
    a = input_people.split(',')
    res = Search(lines, a[2])
    if res == 'Человек не найден':
        c = False
    else:
        Deleted_Date(lines, input_people)
        Append_File()
        c = True
    return c

def Search_in_file():
    with open(file_path, 'r') as f:
        input_people = input('Введите Имя или Фамилию или номер телефона(через +7) для поиска контакта\n')
        print(Search(f, input_people))


def Search(file, i):
    b = False
    res = []
    for line in file:
        line = line.strip('\n')
        a = line.split(',')
        for n in range(0, len(a)):
            if i == a[n]:
                res = line
                b = True
    if not b:
        res = 'Человек не найден'
    return res

def Perform_People():
    perfrom_people = int(input('\nВыберете действие, введя нужную цифру\n' + '1 - вывести данные в файле\n' + '2 - добавить данные в файл\n' + '3 - выполнить поиск определенной записи\n' + '4 - удалить информацию с файла\n' + '5 - изменить данные контакта\n' + '0 - выйти из справочника\n'))
    while perfrom_people != 0:
        if perfrom_people == 1:
            Read_File()
            return Perform_People()
        elif perfrom_people == 2:
            Append_File()
            return Perform_People()
        elif perfrom_people == 3:
            Search_in_file()
            return Perform_People()
        elif perfrom_people == 4:
            Deleted_File()
            return Perform_People()
        elif perfrom_people == 5:
            Change_File()
            return Perform_People()
        else:
            print('Вы ввели неправильный номер действия\n')
            return Perform_People()




Perform_People()
